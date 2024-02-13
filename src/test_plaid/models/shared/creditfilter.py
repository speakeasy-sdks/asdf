"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditaccountsubtype import CreditAccountSubtype
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFilter:
    r"""A filter to apply to `credit`-type accounts"""
    UNSET='__SPEAKEASY_UNSET__'
    account_subtypes: List[CreditAccountSubtype] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_subtypes') }})
    r"""An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema)."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

