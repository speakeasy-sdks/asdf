"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentInitiationPaymentTokenCreateResponse:
    r"""PaymentInitiationPaymentTokenCreateResponse defines the response schema for `/payment_initiation/payment/token/create`"""
    UNSET='__SPEAKEASY_UNSET__'
    payment_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_token') }})
    r"""A `payment_token` that can be provided to Link initialization to enter the payment initiation flow"""
    payment_token_expiration_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_token_expiration_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time at which the token will expire, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. A `payment_token` expires after 15 minutes."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

