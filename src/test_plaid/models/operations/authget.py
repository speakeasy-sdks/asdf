"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import authgetresponse as shared_authgetresponse
from ...models.shared import plaiderror as shared_plaiderror
from typing import Optional


@dataclasses.dataclass
class AuthGetResponse:
    UNSET='__SPEAKEASY_UNSET__'
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    auth_get_response: Optional[shared_authgetresponse.AuthGetResponse] = dataclasses.field(default=None)
    r"""success"""
    plaid_error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=UNSET)
    r"""Default error"""
    

