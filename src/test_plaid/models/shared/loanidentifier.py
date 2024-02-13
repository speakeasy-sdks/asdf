"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .loanidentifiertype import LoanIdentifierType
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoanIdentifier:
    r"""The information used to identify this loan by various parties to the transaction or other organizations."""
    UNSET='__SPEAKEASY_UNSET__'
    loan_identifier: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('LoanIdentifier') }})
    r"""The value of the identifier for the specified type."""
    loan_identifier_type: Optional[LoanIdentifierType] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('LoanIdentifierType') }})
    r"""A value from a MISMO prescribed list that specifies the type of loan identifier."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

