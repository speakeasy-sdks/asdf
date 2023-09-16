"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional



@dataclasses.dataclass
class IdentityVerificationListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    identity_verification_list_response: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

