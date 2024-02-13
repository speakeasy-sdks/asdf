"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionStreamAmount:
    r"""Object with data pertaining to an amount on the transaction stream."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""Represents the numerical value of an amount."""
    iso_currency_code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code'), 'exclude': lambda f: f is TransactionStreamAmount.UNSET }})
    r"""The ISO-4217 currency code of the amount. Always `null` if `unofficial_currency_code` is non-`null`.

    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """
    unofficial_currency_code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unofficial_currency_code'), 'exclude': lambda f: f is TransactionStreamAmount.UNSET }})
    r"""The unofficial currency code of the amount. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries."""
    

