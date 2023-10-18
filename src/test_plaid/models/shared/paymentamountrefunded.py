"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import paymentamountcurrency as shared_paymentamountcurrency
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentAmountRefunded:
    r"""The amount that has been refunded already. Subtract this from the payment amount to calculate the amount still available to refund."""
    currency: shared_paymentamountcurrency.PaymentAmountCurrency = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""The ISO-4217 currency code of the payment. For standing orders and payment consents, `\\"GBP\\"` must be used. For Poland, Denmark, Sweden and Norway, only the local currency is currently supported."""
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""The amount of the payment. Must contain at most two digits of precision e.g. `1.23`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
