"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional



@dataclasses.dataclass
class TransferOriginatorCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plaid_error: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""Error response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    transfer_originator_create_response: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""OK"""
    

