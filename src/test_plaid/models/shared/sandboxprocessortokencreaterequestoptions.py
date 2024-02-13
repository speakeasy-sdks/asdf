"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SandboxProcessorTokenCreateRequestOptions:
    r"""An optional set of options to be used when configuring the Item. If specified, must not be `null`."""
    UNSET='__SPEAKEASY_UNSET__'
    override_password: Optional[str] = dataclasses.field(default='pass_good', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('override_password'), 'exclude': lambda f: f is SandboxProcessorTokenCreateRequestOptions.UNSET }})
    r"""Test password to use for the creation of the Sandbox Item. Default value is `pass_good`."""
    override_username: Optional[str] = dataclasses.field(default='user_good', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('override_username'), 'exclude': lambda f: f is SandboxProcessorTokenCreateRequestOptions.UNSET }})
    r"""Test username to use for the creation of the Sandbox Item. Default value is `user_good`."""
    

