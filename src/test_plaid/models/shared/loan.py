"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .loanidentifiers import LoanIdentifiers
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Loan:
    r"""Information specific to a mortgage loan agreement between one or more borrowers and a mortgage lender."""
    UNSET='__SPEAKEASY_UNSET__'
    loan_identifiers: LoanIdentifiers = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('LOAN_IDENTIFIERS') }})
    r"""Collection of current and previous identifiers for this loan."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

