"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import plaiderror as shared_plaiderror
from ...models.shared import sandboxbankincomefirewebhookresponse as shared_sandboxbankincomefirewebhookresponse
from typing import Optional


@dataclasses.dataclass
class SandboxBankIncomeFireWebhookResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    plaid_error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response"""
    sandbox_bank_income_fire_webhook_response: Optional[shared_sandboxbankincomefirewebhookresponse.SandboxBankIncomeFireWebhookResponse] = dataclasses.field(default=None)
    r"""OK"""
    

