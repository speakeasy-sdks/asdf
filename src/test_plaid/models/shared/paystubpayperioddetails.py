"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditpaystubpaybasistype import CreditPayStubPayBasisType
from .paystubdistributionbreakdown import PayStubDistributionBreakdown
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayStubPayPeriodDetails:
    r"""Details about the pay period."""
    UNSET='__SPEAKEASY_UNSET__'
    distribution_breakdown: List[PayStubDistributionBreakdown] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('distribution_breakdown') }})
    end_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date on which the pay period ended, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\\"yyyy-mm-dd\\")."""
    gross_earnings: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gross_earnings') }})
    r"""Total earnings before tax/deductions."""
    iso_currency_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null."""
    pay_amount: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_amount') }})
    r"""The amount of the paycheck."""
    pay_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date on which the pay stub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\\"yyyy-mm-dd\\")."""
    pay_frequency: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_frequency') }})
    r"""The frequency at which an individual is paid."""
    start_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date on which the pay period started, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\\"yyyy-mm-dd\\")."""
    unofficial_currency_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unofficial_currency_code') }})
    r"""The unofficial currency code associated with the net pay. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.

    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    pay_basis: Optional[CreditPayStubPayBasisType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_basis'), 'exclude': lambda f: f is None }})
    r"""The explicit pay basis on the paystub (if present)."""
    

