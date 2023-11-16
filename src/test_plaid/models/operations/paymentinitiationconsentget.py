"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import paymentinitiationconsentgetresponse as shared_paymentinitiationconsentgetresponse
from typing import Optional


@dataclasses.dataclass
class PaymentInitiationConsentGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    payment_initiation_consent_get_response: Optional[shared_paymentinitiationconsentgetresponse.PaymentInitiationConsentGetResponse] = dataclasses.field(default=None)
    r"""OK"""
    

