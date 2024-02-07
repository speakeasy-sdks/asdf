"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import incomeverificationtaxformsgetresponse as shared_incomeverificationtaxformsgetresponse
from ...models.shared import plaiderror as shared_plaiderror
from typing import Optional


@dataclasses.dataclass
class IncomeVerificationTaxformsGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    income_verification_taxforms_get_response: Optional[shared_incomeverificationtaxformsgetresponse.IncomeVerificationTaxformsGetResponse] = dataclasses.field(default=None)
    r"""OK"""
    plaid_error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response."""
    

