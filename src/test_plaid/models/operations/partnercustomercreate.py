"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import partnercustomercreateresponse as shared_partnercustomercreateresponse
from ...models.shared import plaiderror as shared_plaiderror
from typing import Optional


@dataclasses.dataclass
class PartnerCustomerCreateResponse:
    UNSET='__SPEAKEASY_UNSET__'
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    partner_customer_create_response: Optional[shared_partnercustomercreateresponse.PartnerCustomerCreateResponse] = dataclasses.field(default=None)
    r"""OK"""
    plaid_error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=UNSET)
    r"""Error response"""
    

