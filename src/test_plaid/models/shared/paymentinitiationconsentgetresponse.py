"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .paymentinitiationconsentconstraints import PaymentInitiationConsentConstraints
from .paymentinitiationconsentscope import PaymentInitiationConsentScope
from .paymentinitiationconsentstatus import PaymentInitiationConsentStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentInitiationConsentGetResponse:
    r"""PaymentInitiationConsentGetResponse defines the response schema for `/payment_initation/consent/get`"""
    UNSET='__SPEAKEASY_UNSET__'
    consent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consent_id') }})
    r"""The consent ID."""
    constraints: PaymentInitiationConsentConstraints = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('constraints') }})
    r"""Limitations that will be applied to payments initiated using the payment consent."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Consent creation timestamp, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    recipient_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_id') }})
    r"""The ID of the recipient the payment consent is for."""
    reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference') }})
    r"""A reference for the payment consent."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    scopes: List[PaymentInitiationConsentScope] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scopes') }})
    r"""An array of payment consent scopes."""
    status: PaymentInitiationConsentStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the payment consent.

    `UNAUTHORISED`: Consent created, but requires user authorisation.

    `REJECTED`: Consent authorisation was rejected by the user and/or the bank.

    `AUTHORISED`: Consent is active and ready to be used.

    `REVOKED`: Consent has been revoked and can no longer be used.

    `EXPIRED`: Consent is no longer valid.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

