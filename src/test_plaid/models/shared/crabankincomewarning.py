"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import crabankincomecause as shared_crabankincomecause
from ..shared import crabankincomewarningcode as shared_crabankincomewarningcode
from ..shared import creditbankincomewarningtype as shared_creditbankincomewarningtype
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CraBankIncomeWarning:
    r"""The warning associated with the data that was unavailable for the Bank Income Report."""
    cause: Optional[shared_crabankincomecause.CraBankIncomeCause] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cause'), 'exclude': lambda f: f is None }})
    r"""An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items."""
    warning_code: Optional[shared_crabankincomewarningcode.CraBankIncomeWarningCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warning_code'), 'exclude': lambda f: f is None }})
    r"""The warning code identifies a specific kind of warning.
    `IDENTITY_UNAVAILABLE`: Unable to extract identity for the Item
    `TRANSACTIONS_UNAVAILABLE`: Unable to extract transactions for the Item
    `REPORT_DELETED`: Report deleted due to customer or consumer request
    `DATA_UNAVAILABLE`: No relevant data was found for the Item
    """
    warning_type: Optional[shared_creditbankincomewarningtype.CreditBankIncomeWarningType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warning_type'), 'exclude': lambda f: f is None }})
    r"""The warning type which will always be `BANK_INCOME_WARNING`."""
    

