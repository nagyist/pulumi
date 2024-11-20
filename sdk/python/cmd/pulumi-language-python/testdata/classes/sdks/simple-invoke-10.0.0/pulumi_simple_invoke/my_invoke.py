# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'MyInvokeResult',
    'AwaitableMyInvokeResult',
    'my_invoke',
    'my_invoke_output',
]

@pulumi.output_type
class MyInvokeResult:
    def __init__(__self__, result=None):
        if result and not isinstance(result, str):
            raise TypeError("Expected argument 'result' to be a str")
        pulumi.set(__self__, "result", result)

    @property
    @pulumi.getter
    def result(self) -> str:
        return pulumi.get(self, "result")


class AwaitableMyInvokeResult(MyInvokeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return MyInvokeResult(
            result=self.result)


def my_invoke(value: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableMyInvokeResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['value'] = value
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('simple-invoke:index:myInvoke', __args__, opts=opts, typ=MyInvokeResult).value

    return AwaitableMyInvokeResult(
        result=pulumi.get(__ret__, 'result'))
def my_invoke_output(value: Optional[pulumi.Input[str]] = None,
                     opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[MyInvokeResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['value'] = value
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('simple-invoke:index:myInvoke', __args__, opts=opts, typ=MyInvokeResult)
    return __ret__.apply(lambda __response__: MyInvokeResult(
        result=pulumi.get(__response__, 'result')))
