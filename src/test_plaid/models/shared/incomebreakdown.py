"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import incomebreakdowntype as shared_incomebreakdowntype
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IncomeBreakdown:
    r"""An object representing a breakdown of the different income types on the paystub.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    hours: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hours') }})
    r"""The number of hours logged for this income for this pay period."""
    rate: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rate') }})
    r"""The hourly rate at which the income is paid."""
    total: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    r"""The total pay for this pay period."""
    type: Optional[shared_incomebreakdowntype.IncomeBreakdownType] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of income. Possible values include:
      `\"regular\"`: regular income
      `\"overtime\"`: overtime income
      `\"bonus\"`: bonus income
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
