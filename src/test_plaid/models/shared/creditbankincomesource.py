"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import creditbankincomecategory as shared_creditbankincomecategory
from ..shared import creditbankincomehistoricalsummary as shared_creditbankincomehistoricalsummary
from ..shared import creditbankincomepayfrequency as shared_creditbankincomepayfrequency
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankIncomeSource:
    r"""Detailed information for the income source."""
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id'), 'exclude': lambda f: f is None }})
    r"""Plaid's unique identifier for the account."""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""Maximum of all dates within the specific income sources in the user’s bank account for days requested by the client.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """
    historical_summary: Optional[List[shared_creditbankincomehistoricalsummary.CreditBankIncomeHistoricalSummary]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('historical_summary'), 'exclude': lambda f: f is None }})
    income_category: Optional[shared_creditbankincomecategory.CreditBankIncomeCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income_category'), 'exclude': lambda f: f is None }})
    r"""The income category. Note that the `CASH` value has been deprecated and is used only for existing legacy implementations. It has been replaced by the new categories `CASH_DEPOSIT` (representing cash or check deposits) and `TRANSFER_FROM_APPLICATION` (representing cash transfers originating from apps, such as Zelle or Venmo)."""
    income_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income_description'), 'exclude': lambda f: f is None }})
    r"""The most common name or original description for the underlying income transactions."""
    income_source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income_source_id'), 'exclude': lambda f: f is None }})
    r"""A unique identifier for an income source."""
    pay_frequency: Optional[shared_creditbankincomepayfrequency.CreditBankIncomePayFrequency] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_frequency'), 'exclude': lambda f: f is None }})
    r"""The income pay frequency."""
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""Minimum of all dates within the specific income sources in the user's bank account for days requested by the client.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_amount'), 'exclude': lambda f: f is None }})
    r"""Total amount of earnings in the user’s bank account for the specific income source for days requested by the client."""
    transaction_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_count'), 'exclude': lambda f: f is None }})
    r"""Number of transactions for the income source within the start and end date."""
    

