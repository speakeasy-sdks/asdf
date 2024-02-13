"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentMeta:
    r"""Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.

    If the `transactions` object was returned by a Transactions endpoint such as `/transactions/sync` or `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """
    UNSET='__SPEAKEASY_UNSET__'
    by_order_of: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('by_order_of') }})
    r"""The party initiating a wire transfer. Will be `null` if the transaction is not a wire transfer."""
    payee: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payee') }})
    r"""For transfers, the party that is receiving the transaction."""
    payer: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payer') }})
    r"""For transfers, the party that is paying the transaction."""
    payment_method: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_method') }})
    r"""The type of transfer, e.g. 'ACH'"""
    payment_processor: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_processor') }})
    r"""The name of the payment processor"""
    ppd_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ppd_id') }})
    r"""The ACH PPD ID for the payer."""
    reason: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason') }})
    r"""The payer-supplied description of the transfer."""
    reference_number: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference_number') }})
    r"""The transaction reference number supplied by the financial institution."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

