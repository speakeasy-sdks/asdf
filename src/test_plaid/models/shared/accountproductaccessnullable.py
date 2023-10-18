"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountProductAccessNullable:
    r"""Allow the application to access specific products on this account"""
    account_data: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_data') }})
    r"""Allow the application to access account data. Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    statements: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statements') }})
    r"""Allow the application to access bank statements. Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""
    tax_documents: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_documents') }})
    r"""Allow the application to access tax documents. Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""
    

