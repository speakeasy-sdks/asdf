"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountaccess as shared_accountaccess
from ..shared import productaccess as shared_productaccess
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ScopesNullable:
    r"""The scopes object"""
    accounts: Optional[List[shared_accountaccess.AccountAccess]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts'), 'exclude': lambda f: f is None }})
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    new_accounts: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_accounts') }})
    r"""Allow access to newly opened accounts as they are opened. If unset, defaults to `true`."""
    product_access: Optional[shared_productaccess.ProductAccess] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product_access'), 'exclude': lambda f: f is None }})
    r"""The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to all products allowed."""
    

