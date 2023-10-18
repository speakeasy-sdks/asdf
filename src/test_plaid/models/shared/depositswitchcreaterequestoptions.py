"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DepositSwitchCreateRequestOptions:
    r"""Options to configure the `/deposit_switch/create` request. If provided, cannot be `null`."""
    transaction_item_access_tokens: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_item_access_tokens'), 'exclude': lambda f: f is None }})
    r"""An array of access tokens corresponding to transaction items to use when attempting to match the user to their Payroll Provider. These tokens must be created by the same client id as the one creating the switch, and have access to the transactions product."""
    webhook: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook') }})
    r"""The URL registered to receive webhooks when the status of a deposit switch request has changed."""
    

