"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from test_plaid import utils
from typing import Any, Dict, Optional

class DepositSwitchTargetAccountAccountSubtype(str, Enum):
    r"""The account subtype of the account, either `checking` or `savings`."""
    CHECKING = 'checking'
    SAVINGS = 'savings'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DepositSwitchTargetAccount:
    r"""The deposit switch destination account"""
    UNSET='__SPEAKEASY_UNSET__'
    account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_name') }})
    r"""The name of the deposit switch destination account, as it will be displayed to the end user in the Deposit Switch interface. It is not required to match the name used in online banking."""
    account_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_number') }})
    r"""Account number for deposit switch destination"""
    account_subtype: DepositSwitchTargetAccountAccountSubtype = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_subtype') }})
    r"""The account subtype of the account, either `checking` or `savings`."""
    routing_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routing_number') }})
    r"""Routing number for deposit switch destination"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

