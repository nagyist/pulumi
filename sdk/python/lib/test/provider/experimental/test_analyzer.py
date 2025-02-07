# Copyright 2025, Pulumi Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path
from typing import Any, Optional, TypedDict, Union

import pulumi
from pulumi.provider.experimental.metadata import Metadata
from pulumi.provider.experimental.analyzer import (
    Analyzer,
    DuplicateTypeError,
    InvalidMapKeyError,
    TypeNotFoundError,
    unwrap_input,
    unwrap_output,
)
from pulumi.provider.experimental.component import (
    ComponentDefinition,
    PropertyDefinition,
    PropertyType,
    TypeDefinition,
)

metadata = Metadata("my-component", "0.0.1")


def test_analyze_component():
    class SelfSignedCertificateArgs(TypedDict):
        algorithm: pulumi.Input[str]
        ecdsa_curve: Optional[pulumi.Input[str]]
        bits: Optional[pulumi.Input[int]]

    class SelfSignedCertificate(pulumi.ComponentResource):
        """Component doc string"""

        pem: pulumi.Output[str]
        private_key: pulumi.Output[str]
        ca_cert: pulumi.Output[str]

        def __init__(self, args: SelfSignedCertificateArgs): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(SelfSignedCertificate, Path("test_analyzer"))
    assert component == ComponentDefinition(
        name="SelfSignedCertificate",
        module="test_analyzer",
        description="Component doc string",
        inputs={
            "algorithm": PropertyDefinition(type=PropertyType.STRING),
            "ecdsaCurve": PropertyDefinition(type=PropertyType.STRING, optional=True),
            "bits": PropertyDefinition(type=PropertyType.INTEGER, optional=True),
        },
        inputs_mapping={
            "algorithm": "algorithm",
            "ecdsaCurve": "ecdsa_curve",
            "bits": "bits",
        },
        outputs={
            "pem": PropertyDefinition(type=PropertyType.STRING),
            "privateKey": PropertyDefinition(type=PropertyType.STRING),
            "caCert": PropertyDefinition(type=PropertyType.STRING),
        },
        outputs_mapping={
            "pem": "pem",
            "privateKey": "private_key",
            "caCert": "ca_cert",
        },
    )


def test_analyze_component_no_args():
    class NoArgs(pulumi.ComponentResource): ...

    analyzer = Analyzer(metadata)
    try:
        component = analyzer.analyze_component(NoArgs, Path("test_analyzer"))
        assert False, f"expected an exception, got {component}"
    except Exception as e:
        assert (
            str(e)
            == "ComponentResource 'NoArgs' requires an argument named 'args' with a type annotation in its __init__ method"
        )


def test_analyze_component_empty():
    class Empty(pulumi.ComponentResource):
        def __init__(self, args: dict[str, Any]): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(Empty, Path("test_analyzer"))
    assert component == ComponentDefinition(
        name="Empty",
        module="test_analyzer",
        inputs={},
        inputs_mapping={},
        outputs={},
        outputs_mapping={},
    )


def test_analyze_component_plain_types():
    class Args(TypedDict):
        input_int: int
        input_str: str
        input_float: float
        input_bool: bool

    class Component(pulumi.ComponentResource):
        output_int: pulumi.Output[int]
        output_str: pulumi.Output[str]
        output_float: pulumi.Output[float]
        output_bool: pulumi.Output[bool]

        def __init__(self, args: Args): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(Component, Path("test_analyzer"))
    assert component == ComponentDefinition(
        name="Component",
        module="test_analyzer",
        inputs={
            "inputInt": PropertyDefinition(type=PropertyType.INTEGER),
            "inputStr": PropertyDefinition(type=PropertyType.STRING),
            "inputFloat": PropertyDefinition(type=PropertyType.NUMBER),
            "inputBool": PropertyDefinition(type=PropertyType.BOOLEAN),
        },
        inputs_mapping={
            "inputInt": "input_int",
            "inputStr": "input_str",
            "inputFloat": "input_float",
            "inputBool": "input_bool",
        },
        outputs={
            "outputInt": PropertyDefinition(type=PropertyType.INTEGER),
            "outputStr": PropertyDefinition(type=PropertyType.STRING),
            "outputFloat": PropertyDefinition(type=PropertyType.NUMBER),
            "outputBool": PropertyDefinition(type=PropertyType.BOOLEAN),
        },
        outputs_mapping={
            "outputInt": "output_int",
            "outputStr": "output_str",
            "outputFloat": "output_float",
            "outputBool": "output_bool",
        },
    )


def test_analyze_list_simple():
    class Args(TypedDict):
        list_input: pulumi.Input[list[str]]

    class Component(pulumi.ComponentResource):
        list_output: Optional[pulumi.Output[list[Optional[str]]]]

        def __init__(self, args: Args): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(Component, Path("test_analyzer"))
    assert component == ComponentDefinition(
        name="Component",
        module="test_analyzer",
        inputs={
            "listInput": PropertyDefinition(
                type=PropertyType.ARRAY,
                items=PropertyDefinition(type=PropertyType.STRING),
            )
        },
        inputs_mapping={"listInput": "list_input"},
        outputs={
            "listOutput": PropertyDefinition(
                type=PropertyType.ARRAY,
                items=PropertyDefinition(type=PropertyType.STRING, optional=True),
                optional=True,
            )
        },
        outputs_mapping={"listOutput": "list_output"},
    )


def test_analyze_list_complex():
    class ComplexType(TypedDict):
        name: Optional[pulumi.Input[list[str]]]

    class Args(TypedDict):
        list_input: pulumi.Input[list[ComplexType]]

    class Component(pulumi.ComponentResource):
        list_output: pulumi.Output[list[ComplexType]]

        def __init__(self, args: Args): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(Component, Path("test_analyzer"))
    assert component == ComponentDefinition(
        name="Component",
        module="test_analyzer",
        inputs={
            "listInput": PropertyDefinition(
                type=PropertyType.ARRAY,
                items=PropertyDefinition(ref="#/types/my-component:index:ComplexType"),
            )
        },
        inputs_mapping={"listInput": "list_input"},
        outputs={
            "listOutput": PropertyDefinition(
                type=PropertyType.ARRAY,
                items=PropertyDefinition(ref="#/types/my-component:index:ComplexType"),
            )
        },
        outputs_mapping={"listOutput": "list_output"},
    )
    assert analyzer.type_definitions == {
        "ComplexType": TypeDefinition(
            name="ComplexType",
            module="test_analyzer",
            type="object",
            properties={
                "name": PropertyDefinition(
                    type=PropertyType.ARRAY,
                    items=PropertyDefinition(type=PropertyType.STRING),
                    optional=True,
                ),
            },
            properties_mapping={
                "name": "name",
            },
        )
    }


def test_analyze_dict_non_str_key():
    class Args(TypedDict):
        bad_dict: pulumi.Input[dict[int, str]]

    class Component(pulumi.ComponentResource):
        def __init__(self, args: Args): ...

    analyzer = Analyzer(metadata)
    try:
        analyzer.analyze_component(Component, Path("test_analyzer"))
    except InvalidMapKeyError as e:
        assert str(e) == "map keys must be strings, got 'int' for 'Args.bad_dict'"


def test_analyze_dict_simple():
    class Args(TypedDict):
        dict_input: pulumi.Input[dict[str, int]]

    class Component(pulumi.ComponentResource):
        dict_output: Optional[pulumi.Output[dict[str, Optional[int]]]]

        def __init__(self, args: Args): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(Component, Path("test_analyzer"))
    assert component == ComponentDefinition(
        name="Component",
        module="test_analyzer",
        inputs={
            "dictInput": PropertyDefinition(
                type=PropertyType.OBJECT,
                additional_properties=PropertyDefinition(type=PropertyType.INTEGER),
            )
        },
        inputs_mapping={"dictInput": "dict_input"},
        outputs={
            "dictOutput": PropertyDefinition(
                type=PropertyType.OBJECT,
                additional_properties=PropertyDefinition(
                    type=PropertyType.INTEGER, optional=True
                ),
                optional=True,
            )
        },
        outputs_mapping={"dictOutput": "dict_output"},
    )


def test_analyze_dict_complex():
    class ComplexType(TypedDict):
        name: Optional[pulumi.Input[dict[str, int]]]

    class Args(TypedDict):
        dict_input: pulumi.Input[dict[str, ComplexType]]

    class Component(pulumi.ComponentResource):
        dict_output: Optional[pulumi.Output[dict[str, Optional[ComplexType]]]]

        def __init__(self, args: Args): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(Component, Path("test_analyzer"))
    assert component == ComponentDefinition(
        name="Component",
        module="test_analyzer",
        inputs={
            "dictInput": PropertyDefinition(
                type=PropertyType.OBJECT,
                additional_properties=PropertyDefinition(
                    ref="#/types/my-component:index:ComplexType"
                ),
            )
        },
        inputs_mapping={"dictInput": "dict_input"},
        outputs={
            "dictOutput": PropertyDefinition(
                type=PropertyType.OBJECT,
                additional_properties=PropertyDefinition(
                    ref="#/types/my-component:index:ComplexType", optional=True
                ),
                optional=True,
            )
        },
        outputs_mapping={"dictOutput": "dict_output"},
    )
    assert analyzer.type_definitions == {
        "ComplexType": TypeDefinition(
            name="ComplexType",
            module="test_analyzer",
            type="object",
            properties={
                "name": PropertyDefinition(
                    type=PropertyType.OBJECT,
                    additional_properties=PropertyDefinition(type=PropertyType.INTEGER),
                    optional=True,
                ),
            },
            properties_mapping={
                "name": "name",
            },
        )
    }


def test_analyze_component_complex_type():
    class ComplexType(TypedDict):
        value: pulumi.Input[str]
        optional_value: Optional[pulumi.Input[int]]

    class Args(TypedDict):
        some_complex_type: pulumi.Input[ComplexType]

    class Component(pulumi.ComponentResource):
        complex_output: pulumi.Output[ComplexType]

        def __init__(self, args: Args): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(Component, Path("test_analyzer"))
    assert component == ComponentDefinition(
        name="Component",
        module="test_analyzer",
        inputs={
            "someComplexType": PropertyDefinition(
                ref="#/types/my-component:index:ComplexType"
            ),
        },
        inputs_mapping={"someComplexType": "some_complex_type"},
        outputs={
            "complexOutput": PropertyDefinition(
                ref="#/types/my-component:index:ComplexType"
            )
        },
        outputs_mapping={"complexOutput": "complex_output"},
    )
    assert analyzer.type_definitions == {
        "ComplexType": TypeDefinition(
            name="ComplexType",
            module="test_analyzer",
            type="object",
            properties={
                "value": PropertyDefinition(type=PropertyType.STRING),
                "optionalValue": PropertyDefinition(
                    type=PropertyType.INTEGER, optional=True
                ),
            },
            properties_mapping={
                "value": "value",
                "optionalValue": "optional_value",
            },
        )
    }


def test_analyze_bad_type():
    analyzer = Analyzer(metadata)

    try:
        analyzer.analyze(Path(Path(__file__).parent, "testdata", "bad-type"))
        assert False, "expected an exception"
    except TypeNotFoundError as e:
        assert (
            str(e)
            == "Could not find the type 'DoesntExist'. Ensure it is defined in your source code or is imported."
        )


def test_analyze_duplicate_type():
    analyzer = Analyzer(metadata)

    try:
        analyzer.analyze(Path(Path(__file__).parent, "testdata", "duplicate-type"))
        assert False, "expected an exception"
    except DuplicateTypeError as e:
        assert (
            str(e)
            == "Duplicate type 'MyDuplicateType': "
            + "orginally defined in 'component_a.py', "
            + "but also found in 'component_b.py'"
        )


def test_analyze_duplicate_components():
    analyzer = Analyzer(metadata)

    try:
        analyzer.analyze(
            Path(Path(__file__).parent, "testdata", "duplicate-components")
        )
        assert False, "expected an exception"
    except DuplicateTypeError as e:
        assert (
            str(e)
            == "Duplicate type 'MyComponent': "
            + "orginally defined in 'component_a.py', "
            + "but also found in 'component_b.py'"
        )


def test_analyze_component_self_recursive_complex_type():
    class RecursiveType(TypedDict):
        rec: Optional[pulumi.Input["RecursiveType"]]

    class Args(TypedDict):
        rec: pulumi.Input[RecursiveType]

    class Component(pulumi.ComponentResource):
        rec: pulumi.Output[RecursiveType]

        def __init__(self, args: Args): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(Component, Path("test_analyzer"))
    assert analyzer.type_definitions == {
        "RecursiveType": TypeDefinition(
            name="RecursiveType",
            module="test_analyzer",
            type="object",
            properties={
                "rec": PropertyDefinition(
                    optional=True,
                    ref="#/types/my-component:index:RecursiveType",
                )
            },
            properties_mapping={"rec": "rec"},
        ),
    }
    assert component == ComponentDefinition(
        name="Component",
        module="test_analyzer",
        inputs={
            "rec": PropertyDefinition(ref="#/types/my-component:index:RecursiveType")
        },
        inputs_mapping={"rec": "rec"},
        outputs={
            "rec": PropertyDefinition(ref="#/types/my-component:index:RecursiveType")
        },
        outputs_mapping={"rec": "rec"},
    )


def test_analyze_component_mutually_recursive_complex_types_inline():
    class RecursiveTypeA(TypedDict):
        b: Optional[pulumi.Input["RecursiveTypeB"]]

    class RecursiveTypeB(TypedDict):
        a: Optional[pulumi.Input[RecursiveTypeA]]

    class Args(TypedDict):
        rec: pulumi.Input[RecursiveTypeA]

    class Component(pulumi.ComponentResource):
        rec: pulumi.Output[RecursiveTypeB]
        # rec: pulumi.Output["RecursiveTypeB"]
        # Using a forward ref instead here causes the test to fail because we
        # would never encounter the type as we walk the tree of types that
        # starts with the Component.
        # When doing full analysis via Analyser.analyze, we can handle this case.
        # See test_analyze_component_mutually_recursive_complex_types_file for
        # an example of this.

        def __init__(self, args: Args): ...

    analyzer = Analyzer(metadata)
    component = analyzer.analyze_component(Component, Path("test_analyzer"))
    assert analyzer.type_definitions == {
        "RecursiveTypeA": TypeDefinition(
            name="RecursiveTypeA",
            module="test_analyzer",
            type="object",
            properties={
                "b": PropertyDefinition(
                    optional=True,
                    ref="#/types/my-component:index:RecursiveTypeB",
                )
            },
            properties_mapping={"b": "b"},
        ),
        "RecursiveTypeB": TypeDefinition(
            name="RecursiveTypeB",
            module="test_analyzer",
            type="object",
            properties={
                "a": PropertyDefinition(
                    optional=True,
                    ref="#/types/my-component:index:RecursiveTypeA",
                )
            },
            properties_mapping={"a": "a"},
        ),
    }
    assert component == ComponentDefinition(
        name="Component",
        module="test_analyzer",
        inputs={
            "rec": PropertyDefinition(ref="#/types/my-component:index:RecursiveTypeA")
        },
        inputs_mapping={"rec": "rec"},
        outputs={
            "rec": PropertyDefinition(ref="#/types/my-component:index:RecursiveTypeB")
        },
        outputs_mapping={"rec": "rec"},
    )


def test_analyze_component_mutually_recursive_complex_types_file():
    analyzer = Analyzer(metadata)

    (components, type_definitions) = analyzer.analyze(
        Path(Path(__file__).parent, "testdata", "mutually-recursive")
    )
    assert type_definitions == {
        "RecursiveTypeA": TypeDefinition(
            name="RecursiveTypeA",
            module="component.py",
            type="object",
            properties={
                "b": PropertyDefinition(
                    optional=True,
                    ref="#/types/my-component:index:RecursiveTypeB",
                )
            },
            properties_mapping={"b": "b"},
        ),
        "RecursiveTypeB": TypeDefinition(
            name="RecursiveTypeB",
            module="component.py",
            type="object",
            properties={
                "a": PropertyDefinition(
                    optional=True,
                    ref="#/types/my-component:index:RecursiveTypeA",
                )
            },
            properties_mapping={"a": "a"},
        ),
    }
    assert components == {
        "Component": ComponentDefinition(
            name="Component",
            module="component.py",
            inputs={
                "rec": PropertyDefinition(
                    ref="#/types/my-component:index:RecursiveTypeA"
                )
            },
            inputs_mapping={"rec": "rec"},
            outputs={
                "rec": PropertyDefinition(
                    ref="#/types/my-component:index:RecursiveTypeA"
                )
            },
            outputs_mapping={"rec": "rec"},
        )
    }


def test_unwrap_output():
    str_output = pulumi.Output[str]
    unwrapped = unwrap_output(str_output)
    assert unwrapped == str

    union_output = pulumi.Output[Union[str, int]]
    unwrapped = unwrap_output(union_output)
    assert unwrapped == Union[str, int]

    try:
        not_output = pulumi.Input[str]
        unwrap_output(not_output)
        assert False, "expected an exception"
    except ValueError as e:
        assert "is not an output type" in str(e)


def test_unwrap_input():
    str_input = pulumi.Input[str]
    unwrapped = unwrap_input(str_input)
    assert unwrapped == str

    union_input = pulumi.Input[Union[str, int]]
    unwrapped = unwrap_input(union_input)
    assert unwrapped == Union[str, int]

    try:
        not_input = pulumi.Output[str]
        unwrap_input(not_input)
        assert False, "expected an exception"
    except ValueError as e:
        assert "is not an input type" in str(e)
