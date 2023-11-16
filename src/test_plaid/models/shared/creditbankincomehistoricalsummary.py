"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditamountwithcurrency import CreditAmountWithCurrency
from .creditbankincometransaction import CreditBankIncomeTransaction
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankIncomeHistoricalSummary:
    r"""The end user's monthly summary for the income source(s)."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The end date of the period included in this monthly summary.
    This date will be the last day of the month, unless the month being covered is a partial month because it is the last month included in the summary and the date range being requested does not end with the last day of the month.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """
    iso_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The ISO 4217 currency code of the amount or balance.
    Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The start date of the period covered in this monthly summary.
    This date will be the first day of the month, unless the month being covered is a partial month because it is the first month included in the summary and the date range being requested does not begin with the first day of the month.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_amount'), 'exclude': lambda f: f is None }})
    r"""Total amount of earnings for the income source(s) of the user for the month in the summary.
    This may return an incorrect value if the summary includes income sources in multiple currencies.
    Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    total_amounts: Optional[List[CreditAmountWithCurrency]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_amounts'), 'exclude': lambda f: f is None }})
    r"""Total amount of earnings for the income source(s) of the user for the month in the summary.
    This can contain multiple amounts, with each amount denominated in one unique currency.
    """
    transactions: Optional[List[CreditBankIncomeTransaction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions'), 'exclude': lambda f: f is None }})
    unofficial_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unofficial_currency_code') }})
    r"""The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null.
    Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    

