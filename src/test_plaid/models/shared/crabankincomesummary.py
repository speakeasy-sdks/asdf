"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import crabankincomehistoricalsummary as shared_crabankincomehistoricalsummary
from ..shared import creditamountwithcurrency as shared_creditamountwithcurrency
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CraBankIncomeSummary:
    r"""Summary for bank income across all income sources and items (max history of 730 days)."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The latest date in which all income sources identified by Plaid appear in the user's account.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """
    forecasted_average_monthly_income: Optional[List[shared_creditamountwithcurrency.CreditAmountWithCurrency]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('forecasted_average_monthly_income'), 'exclude': lambda f: f is None }})
    r"""The predicted average monthly income amount for the income source(s)."""
    historical_average_monthly_gross_income: Optional[List[shared_creditamountwithcurrency.CreditAmountWithCurrency]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('historical_average_monthly_gross_income'), 'exclude': lambda f: f is None }})
    r"""An estimate of the average gross monthly income based on the historical net amount and income category for the income source(s)."""
    historical_average_monthly_income: Optional[List[shared_creditamountwithcurrency.CreditAmountWithCurrency]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('historical_average_monthly_income'), 'exclude': lambda f: f is None }})
    r"""The average monthly income amount estimated based on the historical data for the income source(s)."""
    historical_summary: Optional[List[shared_crabankincomehistoricalsummary.CraBankIncomeHistoricalSummary]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('historical_summary'), 'exclude': lambda f: f is None }})
    income_categories_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income_categories_count'), 'exclude': lambda f: f is None }})
    r"""Number of income categories per end user."""
    income_sources_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income_sources_count'), 'exclude': lambda f: f is None }})
    r"""Number of income sources per end user."""
    income_transactions_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income_transactions_count'), 'exclude': lambda f: f is None }})
    r"""Number of income transactions per end user."""
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The earliest date within the days requested in which all income sources identified by Plaid appear in a user's account.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """
    total_amounts: Optional[List[shared_creditamountwithcurrency.CreditAmountWithCurrency]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_amounts'), 'exclude': lambda f: f is None }})
    r"""Total amount of earnings across all the income sources in the end user's Items for the days requested by the client.
    This can contain multiple amounts, with each amount denominated in one unique currency.
    """
    

