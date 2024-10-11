# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'ToSecretResult',
    'AwaitableToSecretResult',
    'to_secret',
    'to_secret_output',
]

@pulumi.output_type
class ToSecretResult:
    def __init__(__self__, bool1=None, bool2=None, bool3=None, int1=None, int2=None, int3=None, list_bool1=None, list_bool2=None, list_bool3=None, list_int1=None, list_int2=None, list_int3=None, list_num1=None, list_num2=None, list_num3=None, list_string1=None, list_string2=None, list_string3=None, map_bool1=None, map_bool2=None, map_bool3=None, map_int1=None, map_int2=None, map_int3=None, map_num1=None, map_num2=None, map_num3=None, map_string1=None, map_string2=None, map_string3=None, num1=None, num2=None, num3=None, obj_bool1=None, obj_bool2=None, obj_bool3=None, obj_int1=None, obj_int2=None, obj_int3=None, obj_num1=None, obj_num2=None, obj_num3=None, obj_string1=None, obj_string2=None, obj_string3=None, string1=None, string2=None, string3=None):
        if bool1 and not isinstance(bool1, bool):
            raise TypeError("Expected argument 'bool1' to be a bool")
        pulumi.set(__self__, "bool1", bool1)
        if bool2 and not isinstance(bool2, bool):
            raise TypeError("Expected argument 'bool2' to be a bool")
        pulumi.set(__self__, "bool2", bool2)
        if bool3 and not isinstance(bool3, bool):
            raise TypeError("Expected argument 'bool3' to be a bool")
        pulumi.set(__self__, "bool3", bool3)
        if int1 and not isinstance(int1, int):
            raise TypeError("Expected argument 'int1' to be a int")
        pulumi.set(__self__, "int1", int1)
        if int2 and not isinstance(int2, int):
            raise TypeError("Expected argument 'int2' to be a int")
        pulumi.set(__self__, "int2", int2)
        if int3 and not isinstance(int3, int):
            raise TypeError("Expected argument 'int3' to be a int")
        pulumi.set(__self__, "int3", int3)
        if list_bool1 and not isinstance(list_bool1, list):
            raise TypeError("Expected argument 'list_bool1' to be a list")
        pulumi.set(__self__, "list_bool1", list_bool1)
        if list_bool2 and not isinstance(list_bool2, list):
            raise TypeError("Expected argument 'list_bool2' to be a list")
        pulumi.set(__self__, "list_bool2", list_bool2)
        if list_bool3 and not isinstance(list_bool3, list):
            raise TypeError("Expected argument 'list_bool3' to be a list")
        pulumi.set(__self__, "list_bool3", list_bool3)
        if list_int1 and not isinstance(list_int1, list):
            raise TypeError("Expected argument 'list_int1' to be a list")
        pulumi.set(__self__, "list_int1", list_int1)
        if list_int2 and not isinstance(list_int2, list):
            raise TypeError("Expected argument 'list_int2' to be a list")
        pulumi.set(__self__, "list_int2", list_int2)
        if list_int3 and not isinstance(list_int3, list):
            raise TypeError("Expected argument 'list_int3' to be a list")
        pulumi.set(__self__, "list_int3", list_int3)
        if list_num1 and not isinstance(list_num1, list):
            raise TypeError("Expected argument 'list_num1' to be a list")
        pulumi.set(__self__, "list_num1", list_num1)
        if list_num2 and not isinstance(list_num2, list):
            raise TypeError("Expected argument 'list_num2' to be a list")
        pulumi.set(__self__, "list_num2", list_num2)
        if list_num3 and not isinstance(list_num3, list):
            raise TypeError("Expected argument 'list_num3' to be a list")
        pulumi.set(__self__, "list_num3", list_num3)
        if list_string1 and not isinstance(list_string1, list):
            raise TypeError("Expected argument 'list_string1' to be a list")
        pulumi.set(__self__, "list_string1", list_string1)
        if list_string2 and not isinstance(list_string2, list):
            raise TypeError("Expected argument 'list_string2' to be a list")
        pulumi.set(__self__, "list_string2", list_string2)
        if list_string3 and not isinstance(list_string3, list):
            raise TypeError("Expected argument 'list_string3' to be a list")
        pulumi.set(__self__, "list_string3", list_string3)
        if map_bool1 and not isinstance(map_bool1, dict):
            raise TypeError("Expected argument 'map_bool1' to be a dict")
        pulumi.set(__self__, "map_bool1", map_bool1)
        if map_bool2 and not isinstance(map_bool2, dict):
            raise TypeError("Expected argument 'map_bool2' to be a dict")
        pulumi.set(__self__, "map_bool2", map_bool2)
        if map_bool3 and not isinstance(map_bool3, dict):
            raise TypeError("Expected argument 'map_bool3' to be a dict")
        pulumi.set(__self__, "map_bool3", map_bool3)
        if map_int1 and not isinstance(map_int1, dict):
            raise TypeError("Expected argument 'map_int1' to be a dict")
        pulumi.set(__self__, "map_int1", map_int1)
        if map_int2 and not isinstance(map_int2, dict):
            raise TypeError("Expected argument 'map_int2' to be a dict")
        pulumi.set(__self__, "map_int2", map_int2)
        if map_int3 and not isinstance(map_int3, dict):
            raise TypeError("Expected argument 'map_int3' to be a dict")
        pulumi.set(__self__, "map_int3", map_int3)
        if map_num1 and not isinstance(map_num1, dict):
            raise TypeError("Expected argument 'map_num1' to be a dict")
        pulumi.set(__self__, "map_num1", map_num1)
        if map_num2 and not isinstance(map_num2, dict):
            raise TypeError("Expected argument 'map_num2' to be a dict")
        pulumi.set(__self__, "map_num2", map_num2)
        if map_num3 and not isinstance(map_num3, dict):
            raise TypeError("Expected argument 'map_num3' to be a dict")
        pulumi.set(__self__, "map_num3", map_num3)
        if map_string1 and not isinstance(map_string1, dict):
            raise TypeError("Expected argument 'map_string1' to be a dict")
        pulumi.set(__self__, "map_string1", map_string1)
        if map_string2 and not isinstance(map_string2, dict):
            raise TypeError("Expected argument 'map_string2' to be a dict")
        pulumi.set(__self__, "map_string2", map_string2)
        if map_string3 and not isinstance(map_string3, dict):
            raise TypeError("Expected argument 'map_string3' to be a dict")
        pulumi.set(__self__, "map_string3", map_string3)
        if num1 and not isinstance(num1, float):
            raise TypeError("Expected argument 'num1' to be a float")
        pulumi.set(__self__, "num1", num1)
        if num2 and not isinstance(num2, float):
            raise TypeError("Expected argument 'num2' to be a float")
        pulumi.set(__self__, "num2", num2)
        if num3 and not isinstance(num3, float):
            raise TypeError("Expected argument 'num3' to be a float")
        pulumi.set(__self__, "num3", num3)
        if obj_bool1 and not isinstance(obj_bool1, dict):
            raise TypeError("Expected argument 'obj_bool1' to be a dict")
        pulumi.set(__self__, "obj_bool1", obj_bool1)
        if obj_bool2 and not isinstance(obj_bool2, dict):
            raise TypeError("Expected argument 'obj_bool2' to be a dict")
        pulumi.set(__self__, "obj_bool2", obj_bool2)
        if obj_bool3 and not isinstance(obj_bool3, dict):
            raise TypeError("Expected argument 'obj_bool3' to be a dict")
        pulumi.set(__self__, "obj_bool3", obj_bool3)
        if obj_int1 and not isinstance(obj_int1, dict):
            raise TypeError("Expected argument 'obj_int1' to be a dict")
        pulumi.set(__self__, "obj_int1", obj_int1)
        if obj_int2 and not isinstance(obj_int2, dict):
            raise TypeError("Expected argument 'obj_int2' to be a dict")
        pulumi.set(__self__, "obj_int2", obj_int2)
        if obj_int3 and not isinstance(obj_int3, dict):
            raise TypeError("Expected argument 'obj_int3' to be a dict")
        pulumi.set(__self__, "obj_int3", obj_int3)
        if obj_num1 and not isinstance(obj_num1, dict):
            raise TypeError("Expected argument 'obj_num1' to be a dict")
        pulumi.set(__self__, "obj_num1", obj_num1)
        if obj_num2 and not isinstance(obj_num2, dict):
            raise TypeError("Expected argument 'obj_num2' to be a dict")
        pulumi.set(__self__, "obj_num2", obj_num2)
        if obj_num3 and not isinstance(obj_num3, dict):
            raise TypeError("Expected argument 'obj_num3' to be a dict")
        pulumi.set(__self__, "obj_num3", obj_num3)
        if obj_string1 and not isinstance(obj_string1, dict):
            raise TypeError("Expected argument 'obj_string1' to be a dict")
        pulumi.set(__self__, "obj_string1", obj_string1)
        if obj_string2 and not isinstance(obj_string2, dict):
            raise TypeError("Expected argument 'obj_string2' to be a dict")
        pulumi.set(__self__, "obj_string2", obj_string2)
        if obj_string3 and not isinstance(obj_string3, dict):
            raise TypeError("Expected argument 'obj_string3' to be a dict")
        pulumi.set(__self__, "obj_string3", obj_string3)
        if string1 and not isinstance(string1, str):
            raise TypeError("Expected argument 'string1' to be a str")
        pulumi.set(__self__, "string1", string1)
        if string2 and not isinstance(string2, str):
            raise TypeError("Expected argument 'string2' to be a str")
        pulumi.set(__self__, "string2", string2)
        if string3 and not isinstance(string3, str):
            raise TypeError("Expected argument 'string3' to be a str")
        pulumi.set(__self__, "string3", string3)

    @property
    @pulumi.getter
    def bool1(self) -> bool:
        return pulumi.get(self, "bool1")

    @property
    @pulumi.getter
    def bool2(self) -> bool:
        return pulumi.get(self, "bool2")

    @property
    @pulumi.getter
    def bool3(self) -> bool:
        return pulumi.get(self, "bool3")

    @property
    @pulumi.getter
    def int1(self) -> int:
        return pulumi.get(self, "int1")

    @property
    @pulumi.getter
    def int2(self) -> int:
        return pulumi.get(self, "int2")

    @property
    @pulumi.getter
    def int3(self) -> int:
        return pulumi.get(self, "int3")

    @property
    @pulumi.getter(name="listBool1")
    def list_bool1(self) -> Sequence[bool]:
        return pulumi.get(self, "list_bool1")

    @property
    @pulumi.getter(name="listBool2")
    def list_bool2(self) -> Sequence[bool]:
        return pulumi.get(self, "list_bool2")

    @property
    @pulumi.getter(name="listBool3")
    def list_bool3(self) -> Sequence[bool]:
        return pulumi.get(self, "list_bool3")

    @property
    @pulumi.getter(name="listInt1")
    def list_int1(self) -> Sequence[int]:
        return pulumi.get(self, "list_int1")

    @property
    @pulumi.getter(name="listInt2")
    def list_int2(self) -> Sequence[int]:
        return pulumi.get(self, "list_int2")

    @property
    @pulumi.getter(name="listInt3")
    def list_int3(self) -> Sequence[int]:
        return pulumi.get(self, "list_int3")

    @property
    @pulumi.getter(name="listNum1")
    def list_num1(self) -> Sequence[float]:
        return pulumi.get(self, "list_num1")

    @property
    @pulumi.getter(name="listNum2")
    def list_num2(self) -> Sequence[float]:
        return pulumi.get(self, "list_num2")

    @property
    @pulumi.getter(name="listNum3")
    def list_num3(self) -> Sequence[float]:
        return pulumi.get(self, "list_num3")

    @property
    @pulumi.getter(name="listString1")
    def list_string1(self) -> Sequence[str]:
        return pulumi.get(self, "list_string1")

    @property
    @pulumi.getter(name="listString2")
    def list_string2(self) -> Sequence[str]:
        return pulumi.get(self, "list_string2")

    @property
    @pulumi.getter(name="listString3")
    def list_string3(self) -> Sequence[str]:
        return pulumi.get(self, "list_string3")

    @property
    @pulumi.getter(name="mapBool1")
    def map_bool1(self) -> Mapping[str, bool]:
        return pulumi.get(self, "map_bool1")

    @property
    @pulumi.getter(name="mapBool2")
    def map_bool2(self) -> Mapping[str, bool]:
        return pulumi.get(self, "map_bool2")

    @property
    @pulumi.getter(name="mapBool3")
    def map_bool3(self) -> Mapping[str, bool]:
        return pulumi.get(self, "map_bool3")

    @property
    @pulumi.getter(name="mapInt1")
    def map_int1(self) -> Mapping[str, int]:
        return pulumi.get(self, "map_int1")

    @property
    @pulumi.getter(name="mapInt2")
    def map_int2(self) -> Mapping[str, int]:
        return pulumi.get(self, "map_int2")

    @property
    @pulumi.getter(name="mapInt3")
    def map_int3(self) -> Mapping[str, int]:
        return pulumi.get(self, "map_int3")

    @property
    @pulumi.getter(name="mapNum1")
    def map_num1(self) -> Mapping[str, float]:
        return pulumi.get(self, "map_num1")

    @property
    @pulumi.getter(name="mapNum2")
    def map_num2(self) -> Mapping[str, float]:
        return pulumi.get(self, "map_num2")

    @property
    @pulumi.getter(name="mapNum3")
    def map_num3(self) -> Mapping[str, float]:
        return pulumi.get(self, "map_num3")

    @property
    @pulumi.getter(name="mapString1")
    def map_string1(self) -> Mapping[str, str]:
        return pulumi.get(self, "map_string1")

    @property
    @pulumi.getter(name="mapString2")
    def map_string2(self) -> Mapping[str, str]:
        return pulumi.get(self, "map_string2")

    @property
    @pulumi.getter(name="mapString3")
    def map_string3(self) -> Mapping[str, str]:
        return pulumi.get(self, "map_string3")

    @property
    @pulumi.getter
    def num1(self) -> float:
        return pulumi.get(self, "num1")

    @property
    @pulumi.getter
    def num2(self) -> float:
        return pulumi.get(self, "num2")

    @property
    @pulumi.getter
    def num3(self) -> float:
        return pulumi.get(self, "num3")

    @property
    @pulumi.getter(name="objBool1")
    def obj_bool1(self) -> 'outputs.Tbool1':
        return pulumi.get(self, "obj_bool1")

    @property
    @pulumi.getter(name="objBool2")
    def obj_bool2(self) -> 'outputs.Tbool2':
        return pulumi.get(self, "obj_bool2")

    @property
    @pulumi.getter(name="objBool3")
    def obj_bool3(self) -> 'outputs.Tbool3':
        return pulumi.get(self, "obj_bool3")

    @property
    @pulumi.getter(name="objInt1")
    def obj_int1(self) -> 'outputs.Tint1':
        return pulumi.get(self, "obj_int1")

    @property
    @pulumi.getter(name="objInt2")
    def obj_int2(self) -> 'outputs.Tint2':
        return pulumi.get(self, "obj_int2")

    @property
    @pulumi.getter(name="objInt3")
    def obj_int3(self) -> 'outputs.Tint3':
        return pulumi.get(self, "obj_int3")

    @property
    @pulumi.getter(name="objNum1")
    def obj_num1(self) -> 'outputs.Tnum1':
        return pulumi.get(self, "obj_num1")

    @property
    @pulumi.getter(name="objNum2")
    def obj_num2(self) -> 'outputs.Tnum2':
        return pulumi.get(self, "obj_num2")

    @property
    @pulumi.getter(name="objNum3")
    def obj_num3(self) -> 'outputs.Tnum3':
        return pulumi.get(self, "obj_num3")

    @property
    @pulumi.getter(name="objString1")
    def obj_string1(self) -> 'outputs.Tstring1':
        return pulumi.get(self, "obj_string1")

    @property
    @pulumi.getter(name="objString2")
    def obj_string2(self) -> 'outputs.Tstring2':
        return pulumi.get(self, "obj_string2")

    @property
    @pulumi.getter(name="objString3")
    def obj_string3(self) -> 'outputs.Tstring3':
        return pulumi.get(self, "obj_string3")

    @property
    @pulumi.getter
    def string1(self) -> str:
        return pulumi.get(self, "string1")

    @property
    @pulumi.getter
    def string2(self) -> str:
        return pulumi.get(self, "string2")

    @property
    @pulumi.getter
    def string3(self) -> str:
        return pulumi.get(self, "string3")


class AwaitableToSecretResult(ToSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ToSecretResult(
            bool1=self.bool1,
            bool2=self.bool2,
            bool3=self.bool3,
            int1=self.int1,
            int2=self.int2,
            int3=self.int3,
            list_bool1=self.list_bool1,
            list_bool2=self.list_bool2,
            list_bool3=self.list_bool3,
            list_int1=self.list_int1,
            list_int2=self.list_int2,
            list_int3=self.list_int3,
            list_num1=self.list_num1,
            list_num2=self.list_num2,
            list_num3=self.list_num3,
            list_string1=self.list_string1,
            list_string2=self.list_string2,
            list_string3=self.list_string3,
            map_bool1=self.map_bool1,
            map_bool2=self.map_bool2,
            map_bool3=self.map_bool3,
            map_int1=self.map_int1,
            map_int2=self.map_int2,
            map_int3=self.map_int3,
            map_num1=self.map_num1,
            map_num2=self.map_num2,
            map_num3=self.map_num3,
            map_string1=self.map_string1,
            map_string2=self.map_string2,
            map_string3=self.map_string3,
            num1=self.num1,
            num2=self.num2,
            num3=self.num3,
            obj_bool1=self.obj_bool1,
            obj_bool2=self.obj_bool2,
            obj_bool3=self.obj_bool3,
            obj_int1=self.obj_int1,
            obj_int2=self.obj_int2,
            obj_int3=self.obj_int3,
            obj_num1=self.obj_num1,
            obj_num2=self.obj_num2,
            obj_num3=self.obj_num3,
            obj_string1=self.obj_string1,
            obj_string2=self.obj_string2,
            obj_string3=self.obj_string3,
            string1=self.string1,
            string2=self.string2,
            string3=self.string3)


def to_secret(bool1: Optional[bool] = None,
              bool2: Optional[bool] = None,
              bool3: Optional[bool] = None,
              int1: Optional[int] = None,
              int2: Optional[int] = None,
              int3: Optional[int] = None,
              list_bool1: Optional[Sequence[bool]] = None,
              list_bool2: Optional[Sequence[bool]] = None,
              list_bool3: Optional[Sequence[bool]] = None,
              list_int1: Optional[Sequence[int]] = None,
              list_int2: Optional[Sequence[int]] = None,
              list_int3: Optional[Sequence[int]] = None,
              list_num1: Optional[Sequence[float]] = None,
              list_num2: Optional[Sequence[float]] = None,
              list_num3: Optional[Sequence[float]] = None,
              list_string1: Optional[Sequence[str]] = None,
              list_string2: Optional[Sequence[str]] = None,
              list_string3: Optional[Sequence[str]] = None,
              map_bool1: Optional[Mapping[str, bool]] = None,
              map_bool2: Optional[Mapping[str, bool]] = None,
              map_bool3: Optional[Mapping[str, bool]] = None,
              map_int1: Optional[Mapping[str, int]] = None,
              map_int2: Optional[Mapping[str, int]] = None,
              map_int3: Optional[Mapping[str, int]] = None,
              map_num1: Optional[Mapping[str, float]] = None,
              map_num2: Optional[Mapping[str, float]] = None,
              map_num3: Optional[Mapping[str, float]] = None,
              map_string1: Optional[Mapping[str, str]] = None,
              map_string2: Optional[Mapping[str, str]] = None,
              map_string3: Optional[Mapping[str, str]] = None,
              num1: Optional[float] = None,
              num2: Optional[float] = None,
              num3: Optional[float] = None,
              obj_bool1: Optional[pulumi.InputType['Tbool1']] = None,
              obj_bool2: Optional[pulumi.InputType['Tbool2']] = None,
              obj_bool3: Optional[pulumi.InputType['Tbool3']] = None,
              obj_int1: Optional[pulumi.InputType['Tint1']] = None,
              obj_int2: Optional[pulumi.InputType['Tint2']] = None,
              obj_int3: Optional[pulumi.InputType['Tint3']] = None,
              obj_num1: Optional[pulumi.InputType['Tnum1']] = None,
              obj_num2: Optional[pulumi.InputType['Tnum2']] = None,
              obj_num3: Optional[pulumi.InputType['Tnum3']] = None,
              obj_string1: Optional[pulumi.InputType['Tstring1']] = None,
              obj_string2: Optional[pulumi.InputType['Tstring2']] = None,
              obj_string3: Optional[pulumi.InputType['Tstring3']] = None,
              string1: Optional[str] = None,
              string2: Optional[str] = None,
              string3: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableToSecretResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['bool1'] = bool1
    __args__['bool2'] = bool2
    __args__['bool3'] = bool3
    __args__['int1'] = int1
    __args__['int2'] = int2
    __args__['int3'] = int3
    __args__['listBool1'] = list_bool1
    __args__['listBool2'] = list_bool2
    __args__['listBool3'] = list_bool3
    __args__['listInt1'] = list_int1
    __args__['listInt2'] = list_int2
    __args__['listInt3'] = list_int3
    __args__['listNum1'] = list_num1
    __args__['listNum2'] = list_num2
    __args__['listNum3'] = list_num3
    __args__['listString1'] = list_string1
    __args__['listString2'] = list_string2
    __args__['listString3'] = list_string3
    __args__['mapBool1'] = map_bool1
    __args__['mapBool2'] = map_bool2
    __args__['mapBool3'] = map_bool3
    __args__['mapInt1'] = map_int1
    __args__['mapInt2'] = map_int2
    __args__['mapInt3'] = map_int3
    __args__['mapNum1'] = map_num1
    __args__['mapNum2'] = map_num2
    __args__['mapNum3'] = map_num3
    __args__['mapString1'] = map_string1
    __args__['mapString2'] = map_string2
    __args__['mapString3'] = map_string3
    __args__['num1'] = num1
    __args__['num2'] = num2
    __args__['num3'] = num3
    __args__['objBool1'] = obj_bool1
    __args__['objBool2'] = obj_bool2
    __args__['objBool3'] = obj_bool3
    __args__['objInt1'] = obj_int1
    __args__['objInt2'] = obj_int2
    __args__['objInt3'] = obj_int3
    __args__['objNum1'] = obj_num1
    __args__['objNum2'] = obj_num2
    __args__['objNum3'] = obj_num3
    __args__['objString1'] = obj_string1
    __args__['objString2'] = obj_string2
    __args__['objString3'] = obj_string3
    __args__['string1'] = string1
    __args__['string2'] = string2
    __args__['string3'] = string3
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('config-grpc:index:toSecret', __args__, opts=opts, typ=ToSecretResult).value

    return AwaitableToSecretResult(
        bool1=pulumi.get(__ret__, 'bool1'),
        bool2=pulumi.get(__ret__, 'bool2'),
        bool3=pulumi.get(__ret__, 'bool3'),
        int1=pulumi.get(__ret__, 'int1'),
        int2=pulumi.get(__ret__, 'int2'),
        int3=pulumi.get(__ret__, 'int3'),
        list_bool1=pulumi.get(__ret__, 'list_bool1'),
        list_bool2=pulumi.get(__ret__, 'list_bool2'),
        list_bool3=pulumi.get(__ret__, 'list_bool3'),
        list_int1=pulumi.get(__ret__, 'list_int1'),
        list_int2=pulumi.get(__ret__, 'list_int2'),
        list_int3=pulumi.get(__ret__, 'list_int3'),
        list_num1=pulumi.get(__ret__, 'list_num1'),
        list_num2=pulumi.get(__ret__, 'list_num2'),
        list_num3=pulumi.get(__ret__, 'list_num3'),
        list_string1=pulumi.get(__ret__, 'list_string1'),
        list_string2=pulumi.get(__ret__, 'list_string2'),
        list_string3=pulumi.get(__ret__, 'list_string3'),
        map_bool1=pulumi.get(__ret__, 'map_bool1'),
        map_bool2=pulumi.get(__ret__, 'map_bool2'),
        map_bool3=pulumi.get(__ret__, 'map_bool3'),
        map_int1=pulumi.get(__ret__, 'map_int1'),
        map_int2=pulumi.get(__ret__, 'map_int2'),
        map_int3=pulumi.get(__ret__, 'map_int3'),
        map_num1=pulumi.get(__ret__, 'map_num1'),
        map_num2=pulumi.get(__ret__, 'map_num2'),
        map_num3=pulumi.get(__ret__, 'map_num3'),
        map_string1=pulumi.get(__ret__, 'map_string1'),
        map_string2=pulumi.get(__ret__, 'map_string2'),
        map_string3=pulumi.get(__ret__, 'map_string3'),
        num1=pulumi.get(__ret__, 'num1'),
        num2=pulumi.get(__ret__, 'num2'),
        num3=pulumi.get(__ret__, 'num3'),
        obj_bool1=pulumi.get(__ret__, 'obj_bool1'),
        obj_bool2=pulumi.get(__ret__, 'obj_bool2'),
        obj_bool3=pulumi.get(__ret__, 'obj_bool3'),
        obj_int1=pulumi.get(__ret__, 'obj_int1'),
        obj_int2=pulumi.get(__ret__, 'obj_int2'),
        obj_int3=pulumi.get(__ret__, 'obj_int3'),
        obj_num1=pulumi.get(__ret__, 'obj_num1'),
        obj_num2=pulumi.get(__ret__, 'obj_num2'),
        obj_num3=pulumi.get(__ret__, 'obj_num3'),
        obj_string1=pulumi.get(__ret__, 'obj_string1'),
        obj_string2=pulumi.get(__ret__, 'obj_string2'),
        obj_string3=pulumi.get(__ret__, 'obj_string3'),
        string1=pulumi.get(__ret__, 'string1'),
        string2=pulumi.get(__ret__, 'string2'),
        string3=pulumi.get(__ret__, 'string3'))
def to_secret_output(bool1: Optional[pulumi.Input[Optional[bool]]] = None,
                     bool2: Optional[pulumi.Input[Optional[bool]]] = None,
                     bool3: Optional[pulumi.Input[Optional[bool]]] = None,
                     int1: Optional[pulumi.Input[Optional[int]]] = None,
                     int2: Optional[pulumi.Input[Optional[int]]] = None,
                     int3: Optional[pulumi.Input[Optional[int]]] = None,
                     list_bool1: Optional[pulumi.Input[Optional[Sequence[bool]]]] = None,
                     list_bool2: Optional[pulumi.Input[Optional[Sequence[bool]]]] = None,
                     list_bool3: Optional[pulumi.Input[Optional[Sequence[bool]]]] = None,
                     list_int1: Optional[pulumi.Input[Optional[Sequence[int]]]] = None,
                     list_int2: Optional[pulumi.Input[Optional[Sequence[int]]]] = None,
                     list_int3: Optional[pulumi.Input[Optional[Sequence[int]]]] = None,
                     list_num1: Optional[pulumi.Input[Optional[Sequence[float]]]] = None,
                     list_num2: Optional[pulumi.Input[Optional[Sequence[float]]]] = None,
                     list_num3: Optional[pulumi.Input[Optional[Sequence[float]]]] = None,
                     list_string1: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     list_string2: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     list_string3: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     map_bool1: Optional[pulumi.Input[Optional[Mapping[str, bool]]]] = None,
                     map_bool2: Optional[pulumi.Input[Optional[Mapping[str, bool]]]] = None,
                     map_bool3: Optional[pulumi.Input[Optional[Mapping[str, bool]]]] = None,
                     map_int1: Optional[pulumi.Input[Optional[Mapping[str, int]]]] = None,
                     map_int2: Optional[pulumi.Input[Optional[Mapping[str, int]]]] = None,
                     map_int3: Optional[pulumi.Input[Optional[Mapping[str, int]]]] = None,
                     map_num1: Optional[pulumi.Input[Optional[Mapping[str, float]]]] = None,
                     map_num2: Optional[pulumi.Input[Optional[Mapping[str, float]]]] = None,
                     map_num3: Optional[pulumi.Input[Optional[Mapping[str, float]]]] = None,
                     map_string1: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                     map_string2: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                     map_string3: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                     num1: Optional[pulumi.Input[Optional[float]]] = None,
                     num2: Optional[pulumi.Input[Optional[float]]] = None,
                     num3: Optional[pulumi.Input[Optional[float]]] = None,
                     obj_bool1: Optional[pulumi.Input[Optional[pulumi.InputType['Tbool1']]]] = None,
                     obj_bool2: Optional[pulumi.Input[Optional[pulumi.InputType['Tbool2']]]] = None,
                     obj_bool3: Optional[pulumi.Input[Optional[pulumi.InputType['Tbool3']]]] = None,
                     obj_int1: Optional[pulumi.Input[Optional[pulumi.InputType['Tint1']]]] = None,
                     obj_int2: Optional[pulumi.Input[Optional[pulumi.InputType['Tint2']]]] = None,
                     obj_int3: Optional[pulumi.Input[Optional[pulumi.InputType['Tint3']]]] = None,
                     obj_num1: Optional[pulumi.Input[Optional[pulumi.InputType['Tnum1']]]] = None,
                     obj_num2: Optional[pulumi.Input[Optional[pulumi.InputType['Tnum2']]]] = None,
                     obj_num3: Optional[pulumi.Input[Optional[pulumi.InputType['Tnum3']]]] = None,
                     obj_string1: Optional[pulumi.Input[Optional[pulumi.InputType['Tstring1']]]] = None,
                     obj_string2: Optional[pulumi.Input[Optional[pulumi.InputType['Tstring2']]]] = None,
                     obj_string3: Optional[pulumi.Input[Optional[pulumi.InputType['Tstring3']]]] = None,
                     string1: Optional[pulumi.Input[Optional[str]]] = None,
                     string2: Optional[pulumi.Input[Optional[str]]] = None,
                     string3: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ToSecretResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['bool1'] = bool1
    __args__['bool2'] = bool2
    __args__['bool3'] = bool3
    __args__['int1'] = int1
    __args__['int2'] = int2
    __args__['int3'] = int3
    __args__['listBool1'] = list_bool1
    __args__['listBool2'] = list_bool2
    __args__['listBool3'] = list_bool3
    __args__['listInt1'] = list_int1
    __args__['listInt2'] = list_int2
    __args__['listInt3'] = list_int3
    __args__['listNum1'] = list_num1
    __args__['listNum2'] = list_num2
    __args__['listNum3'] = list_num3
    __args__['listString1'] = list_string1
    __args__['listString2'] = list_string2
    __args__['listString3'] = list_string3
    __args__['mapBool1'] = map_bool1
    __args__['mapBool2'] = map_bool2
    __args__['mapBool3'] = map_bool3
    __args__['mapInt1'] = map_int1
    __args__['mapInt2'] = map_int2
    __args__['mapInt3'] = map_int3
    __args__['mapNum1'] = map_num1
    __args__['mapNum2'] = map_num2
    __args__['mapNum3'] = map_num3
    __args__['mapString1'] = map_string1
    __args__['mapString2'] = map_string2
    __args__['mapString3'] = map_string3
    __args__['num1'] = num1
    __args__['num2'] = num2
    __args__['num3'] = num3
    __args__['objBool1'] = obj_bool1
    __args__['objBool2'] = obj_bool2
    __args__['objBool3'] = obj_bool3
    __args__['objInt1'] = obj_int1
    __args__['objInt2'] = obj_int2
    __args__['objInt3'] = obj_int3
    __args__['objNum1'] = obj_num1
    __args__['objNum2'] = obj_num2
    __args__['objNum3'] = obj_num3
    __args__['objString1'] = obj_string1
    __args__['objString2'] = obj_string2
    __args__['objString3'] = obj_string3
    __args__['string1'] = string1
    __args__['string2'] = string2
    __args__['string3'] = string3
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('config-grpc:index:toSecret', __args__, opts=opts, typ=ToSecretResult)
    return __ret__.apply(lambda __response__: ToSecretResult(
        bool1=pulumi.get(__response__, 'bool1'),
        bool2=pulumi.get(__response__, 'bool2'),
        bool3=pulumi.get(__response__, 'bool3'),
        int1=pulumi.get(__response__, 'int1'),
        int2=pulumi.get(__response__, 'int2'),
        int3=pulumi.get(__response__, 'int3'),
        list_bool1=pulumi.get(__response__, 'list_bool1'),
        list_bool2=pulumi.get(__response__, 'list_bool2'),
        list_bool3=pulumi.get(__response__, 'list_bool3'),
        list_int1=pulumi.get(__response__, 'list_int1'),
        list_int2=pulumi.get(__response__, 'list_int2'),
        list_int3=pulumi.get(__response__, 'list_int3'),
        list_num1=pulumi.get(__response__, 'list_num1'),
        list_num2=pulumi.get(__response__, 'list_num2'),
        list_num3=pulumi.get(__response__, 'list_num3'),
        list_string1=pulumi.get(__response__, 'list_string1'),
        list_string2=pulumi.get(__response__, 'list_string2'),
        list_string3=pulumi.get(__response__, 'list_string3'),
        map_bool1=pulumi.get(__response__, 'map_bool1'),
        map_bool2=pulumi.get(__response__, 'map_bool2'),
        map_bool3=pulumi.get(__response__, 'map_bool3'),
        map_int1=pulumi.get(__response__, 'map_int1'),
        map_int2=pulumi.get(__response__, 'map_int2'),
        map_int3=pulumi.get(__response__, 'map_int3'),
        map_num1=pulumi.get(__response__, 'map_num1'),
        map_num2=pulumi.get(__response__, 'map_num2'),
        map_num3=pulumi.get(__response__, 'map_num3'),
        map_string1=pulumi.get(__response__, 'map_string1'),
        map_string2=pulumi.get(__response__, 'map_string2'),
        map_string3=pulumi.get(__response__, 'map_string3'),
        num1=pulumi.get(__response__, 'num1'),
        num2=pulumi.get(__response__, 'num2'),
        num3=pulumi.get(__response__, 'num3'),
        obj_bool1=pulumi.get(__response__, 'obj_bool1'),
        obj_bool2=pulumi.get(__response__, 'obj_bool2'),
        obj_bool3=pulumi.get(__response__, 'obj_bool3'),
        obj_int1=pulumi.get(__response__, 'obj_int1'),
        obj_int2=pulumi.get(__response__, 'obj_int2'),
        obj_int3=pulumi.get(__response__, 'obj_int3'),
        obj_num1=pulumi.get(__response__, 'obj_num1'),
        obj_num2=pulumi.get(__response__, 'obj_num2'),
        obj_num3=pulumi.get(__response__, 'obj_num3'),
        obj_string1=pulumi.get(__response__, 'obj_string1'),
        obj_string2=pulumi.get(__response__, 'obj_string2'),
        obj_string3=pulumi.get(__response__, 'obj_string3'),
        string1=pulumi.get(__response__, 'string1'),
        string2=pulumi.get(__response__, 'string2'),
        string3=pulumi.get(__response__, 'string3')))
