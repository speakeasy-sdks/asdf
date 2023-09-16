"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import depositswitchcreaterequestoptions as shared_depositswitchcreaterequestoptions
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from test_plaid import utils
from typing import Any, Optional

class DepositSwitchAltCreateRequestCountryCode(str, Enum):
    r"""ISO-3166-1 alpha-2 country code standard."""
    US = 'US'
    CA = 'CA'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DepositSwitchAltCreateRequest:
    r"""DepositSwitchAltCreateRequest defines the request schema for `/deposit_switch/alt/create`"""
    target_account: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_account') }})
    r"""The deposit switch destination account"""
    target_user: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_user') }})
    r"""The deposit switch target user"""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    country_code: Optional[DepositSwitchAltCreateRequestCountryCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_code'), 'exclude': lambda f: f is None }})
    r"""ISO-3166-1 alpha-2 country code standard."""
    options: Optional[shared_depositswitchcreaterequestoptions.DepositSwitchCreateRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""Options to configure the `/deposit_switch/create` request. If provided, cannot be `null`."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

