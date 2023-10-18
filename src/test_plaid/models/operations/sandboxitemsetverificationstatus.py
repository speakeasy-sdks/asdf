"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import sandboxitemsetverificationstatusresponse as shared_sandboxitemsetverificationstatusresponse
from typing import Optional


@dataclasses.dataclass
class SandboxItemSetVerificationStatusResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    sandbox_item_set_verification_status_response: Optional[shared_sandboxitemsetverificationstatusresponse.SandboxItemSetVerificationStatusResponse] = dataclasses.field(default=None)
    r"""OK"""
    

