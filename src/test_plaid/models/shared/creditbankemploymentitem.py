"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import creditbankemployment as shared_creditbankemployment
from ..shared import creditbankincomeaccount as shared_creditbankincomeaccount
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankEmploymentItem:
    r"""The details and metadata for an end user's Item."""
    bank_employment_accounts: List[shared_creditbankincomeaccount.CreditBankIncomeAccount] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_employment_accounts') }})
    r"""The Item's accounts that have Bank Employment data."""
    bank_employments: List[shared_creditbankemployment.CreditBankEmployment] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_employments') }})
    r"""The bank employment information for this Item. Each entry in the array is a different employer found."""
    institution_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_id') }})
    r"""The unique identifier of the institution associated with the Item."""
    institution_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_name') }})
    r"""The name of the institution associated with the Item."""
    item_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item_id') }})
    r"""The unique identifier for the Item."""
    last_updated_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_updated_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The time when this Item's data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \\"2018-04-12T03:32:11Z\\")."""
    

