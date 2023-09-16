"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InvestmentsAuthGetRequestOptions:
    r"""An optional object to filter `/investments/auth/get` results."""
    account_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_ids'), 'exclude': lambda f: f is None }})
    r"""An array of `account_id`s to retrieve for the Item. An error will be returned if a provided `account_id` is not associated with the Item."""
    

