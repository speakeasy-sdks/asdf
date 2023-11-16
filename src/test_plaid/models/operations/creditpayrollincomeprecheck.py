"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import creditpayrollincomeprecheckresponse as shared_creditpayrollincomeprecheckresponse
from typing import Optional


@dataclasses.dataclass
class CreditPayrollIncomePrecheckResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    credit_payroll_income_precheck_response: Optional[shared_creditpayrollincomeprecheckresponse.CreditPayrollIncomePrecheckResponse] = dataclasses.field(default=None)
    r"""OK"""
    

