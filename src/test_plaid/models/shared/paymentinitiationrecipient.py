"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .paymentinitiationaddress import PaymentInitiationAddress
from .recipientbacsnullable import RecipientBACSNullable
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentInitiationRecipient:
    r"""PaymentInitiationRecipient defines a payment initiation recipient"""
    UNSET='__SPEAKEASY_UNSET__'
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the recipient."""
    recipient_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_id') }})
    r"""The ID of the recipient."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    address: Optional[PaymentInitiationAddress] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is PaymentInitiationRecipient.UNSET }})
    r"""The optional address of the payment recipient's bank account. Required by most institutions outside of the UK."""
    bacs: Optional[RecipientBACSNullable] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bacs'), 'exclude': lambda f: f is PaymentInitiationRecipient.UNSET }})
    r"""An object containing a BACS account number and sort code. If an IBAN is not provided or if this recipient needs to accept domestic GBP-denominated payments, BACS data is required."""
    iban: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iban'), 'exclude': lambda f: f is PaymentInitiationRecipient.UNSET }})
    r"""The International Bank Account Number (IBAN) for the recipient."""
    

