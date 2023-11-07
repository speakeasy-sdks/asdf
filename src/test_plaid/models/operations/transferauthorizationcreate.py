"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import plaiderror as shared_plaiderror
from ...models.shared import transferauthorizationcreateresponse as shared_transferauthorizationcreateresponse
from typing import Optional


@dataclasses.dataclass
class TransferAuthorizationCreateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    plaid_error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    transfer_authorization_create_response: Optional[shared_transferauthorizationcreateresponse.TransferAuthorizationCreateResponse] = dataclasses.field(default=None)
    r"""OK"""
    

