"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import paymentamount as shared_paymentamount
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PaymentInitiationConsentPaymentExecuteRequest:
    r"""PaymentInitiationConsentPaymentExecuteRequest defines the request schema for `/payment_initiation/consent/payment/execute`"""
    amount: shared_paymentamount.PaymentAmount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount and currency of a payment"""
    consent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consent_id') }})
    r"""The consent ID."""
    idempotency_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('idempotency_key') }})
    r"""A random key provided by the client, per unique consent payment. Maximum of 128 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. If a request to execute a consent payment fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single payment is created. If the request was successfully processed, it will prevent any payment that uses the same idempotency key, and was received within 24 hours of the first request, from being processed.
    """
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

