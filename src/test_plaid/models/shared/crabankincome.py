"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import crabankincomeitem as shared_crabankincomeitem
from ..shared import crabankincomesummary as shared_crabankincomesummary
from ..shared import crabankincomewarning as shared_crabankincomewarning
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CraBankIncome:
    r"""The report of the Bank Income data for an end user."""
    bank_income_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_income_id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier associated with the Bank Income Report."""
    bank_income_summary: Optional[shared_crabankincomesummary.CraBankIncomeSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_income_summary'), 'exclude': lambda f: f is None }})
    r"""Summary for bank income across all income sources and items (max history of 730 days)."""
    days_requested: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_requested'), 'exclude': lambda f: f is None }})
    r"""The number of days requested by the customer for the Bank Income Report."""
    generated_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generated_time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The time when the Bank Income Report was generated."""
    items: Optional[List[shared_crabankincomeitem.CraBankIncomeItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    r"""The list of Items in the report along with the associated metadata about the Item."""
    warnings: Optional[List[shared_crabankincomewarning.CraBankIncomeWarning]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})
    r"""If data from the Bank Income report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete."""
    
