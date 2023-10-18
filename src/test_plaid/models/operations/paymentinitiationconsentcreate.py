"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import paymentinitiationconsentcreateresponse as shared_paymentinitiationconsentcreateresponse
from typing import Optional


@dataclasses.dataclass
class PaymentInitiationConsentCreateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    payment_initiation_consent_create_response: Optional[shared_paymentinitiationconsentcreateresponse.PaymentInitiationConsentCreateResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

