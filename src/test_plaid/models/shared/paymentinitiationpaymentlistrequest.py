"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentInitiationPaymentListRequest:
    r"""PaymentInitiationPaymentListRequest defines the request schema for `/payment_initiation/payment/list`"""
    UNSET='__SPEAKEASY_UNSET__'
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    consent_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consent_id'), 'exclude': lambda f: f is PaymentInitiationPaymentListRequest.UNSET }})
    r"""The consent ID. If specified, only payments, executed using this consent, will be returned."""
    count: Optional[int] = dataclasses.field(default=10, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count'), 'exclude': lambda f: f is PaymentInitiationPaymentListRequest.UNSET }})
    r"""The maximum number of payments to return. If `count` is not specified, a maximum of 10 payments will be returned, beginning with the most recent payment before the cursor (if specified)."""
    cursor: Optional[datetime] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursor'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is PaymentInitiationPaymentListRequest.UNSET }})
    r"""A string in RFC 3339 format (i.e. \\"2019-12-06T22:35:49Z\\"). Only payments created before the cursor will be returned."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

