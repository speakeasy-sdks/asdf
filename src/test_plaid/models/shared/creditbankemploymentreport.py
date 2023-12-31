"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .creditbankemploymentitem import CreditBankEmploymentItem
from .creditbankemploymentwarning import CreditBankEmploymentWarning
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankEmploymentReport:
    r"""The report of the Bank Employment data for an end user."""
    bank_employment_report_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_employment_report_id') }})
    r"""The unique identifier associated with the Bank Employment Report."""
    days_requested: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_requested') }})
    r"""The number of days requested by the customer for the Bank Employment Report."""
    generated_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generated_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The time when the Bank Employment Report was generated, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \\"2018-04-12T03:32:11Z\\")."""
    items: List[CreditBankEmploymentItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    r"""The list of Items in the report along with the associated metadata about the Item."""
    warnings: List[CreditBankEmploymentWarning] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings') }})
    r"""If data from the Bank Employment report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete."""
    

