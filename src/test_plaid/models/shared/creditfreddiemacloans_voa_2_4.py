"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfreddiemacloan_voa_2_4 import CreditFreddieMacLoanVOA24
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacLoansVOA24:
    r"""A collection of loans that are part of a single deal."""
    loan: CreditFreddieMacLoanVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('LOAN') }})
    r"""Information specific to a mortgage loan agreement between one or more borrowers and a mortgage lender."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

