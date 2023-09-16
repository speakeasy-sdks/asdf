"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from test_plaid import utils
from typing import Optional

class SandboxItemSetVerificationStatusRequestVerificationStatus(str, Enum):
    r"""The verification status to set the account to."""
    AUTOMATICALLY_VERIFIED = 'automatically_verified'
    VERIFICATION_EXPIRED = 'verification_expired'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SandboxItemSetVerificationStatusRequest:
    r"""SandboxItemSetVerificationStatusRequest defines the request schema for `/sandbox/item/set_verification_status`"""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The access token associated with the Item data is being requested for."""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The `account_id` of the account whose verification status is to be modified"""
    verification_status: SandboxItemSetVerificationStatusRequestVerificationStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verification_status') }})
    r"""The verification status to set the account to."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    
