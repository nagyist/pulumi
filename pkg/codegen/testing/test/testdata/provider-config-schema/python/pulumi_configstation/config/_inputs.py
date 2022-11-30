# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'SandwichArgs',
]

@pulumi.input_type
class SandwichArgs:
    def __init__(__self__, *,
                 bread: Optional[pulumi.Input[str]] = None,
                 veggies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        if bread is not None:
            pulumi.set(__self__, "bread", bread)
        if veggies is not None:
            pulumi.set(__self__, "veggies", veggies)

    @property
    @pulumi.getter
    def bread(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bread")

    @bread.setter
    def bread(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bread", value)

    @property
    @pulumi.getter
    def veggies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "veggies")

    @veggies.setter
    def veggies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "veggies", value)


