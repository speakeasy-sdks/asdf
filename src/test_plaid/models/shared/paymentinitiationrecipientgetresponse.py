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
class PaymentInitiationRecipientGetResponse:
    r"""PaymentInitiationRecipientGetResponse defines the response schema for `/payment_initiation/recipient/get`"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the recipient."""
    recipient_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_id') }})
    r"""The ID of the recipient."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    address: Optional[PaymentInitiationAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""The optional address of the payment recipient's bank account. Required by most institutions outside of the UK."""
    bacs: Optional[RecipientBACSNullable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bacs') }})
    r"""An object containing a BACS account number and sort code. If an IBAN is not provided or if this recipient needs to accept domestic GBP-denominated payments, BACS data is required."""
    iban: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iban') }})
    r"""The International Bank Account Number (IBAN) for the recipient."""
    

