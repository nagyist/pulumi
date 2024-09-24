# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'Data',
]

@pulumi.output_type
class Data(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "boolArray":
            suggest = "bool_array"
        elif key == "stringMap":
            suggest = "string_map"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Data. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Data.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Data.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bool_array: Sequence[bool],
                 boolean: bool,
                 float: float,
                 integer: int,
                 string: str,
                 string_map: Mapping[str, str]):
        pulumi.set(__self__, "bool_array", bool_array)
        pulumi.set(__self__, "boolean", boolean)
        pulumi.set(__self__, "float", float)
        pulumi.set(__self__, "integer", integer)
        pulumi.set(__self__, "string", string)
        pulumi.set(__self__, "string_map", string_map)

    @property
    @pulumi.getter(name="boolArray")
    def bool_array(self) -> Sequence[bool]:
        return pulumi.get(self, "bool_array")

    @property
    @pulumi.getter
    def boolean(self) -> bool:
        return pulumi.get(self, "boolean")

    @property
    @pulumi.getter
    def float(self) -> float:
        return pulumi.get(self, "float")

    @property
    @pulumi.getter
    def integer(self) -> int:
        return pulumi.get(self, "integer")

    @property
    @pulumi.getter
    def string(self) -> str:
        return pulumi.get(self, "string")

    @property
    @pulumi.getter(name="stringMap")
    def string_map(self) -> Mapping[str, str]:
        return pulumi.get(self, "string_map")


