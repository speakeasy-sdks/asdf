"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import statementsstatement as shared_statementsstatement
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StatementsAccount:
    r"""Account associated with the item."""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""Plaid's unique identifier for the account."""
    account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_name') }})
    r"""The name of the account, either assigned by the user or by the financial institution itself."""
    account_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_type') }})
    r"""The type of account. Possible values are investment, credit, depository, loan, brokerage, other."""
    statements: List[shared_statementsstatement.StatementsStatement] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statements') }})
    r"""The list of statements' metadata associated with this account."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

