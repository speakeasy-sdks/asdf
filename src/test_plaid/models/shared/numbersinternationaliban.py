"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NumbersInternationalIBAN:
    r"""Account numbers using the International Bank Account Number and BIC/SWIFT code format."""
    bic: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bic') }})
    r"""The Business Identifier Code, also known as SWIFT code, for this bank account."""
    iban: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iban') }})
    r"""International Bank Account Number (IBAN)."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

