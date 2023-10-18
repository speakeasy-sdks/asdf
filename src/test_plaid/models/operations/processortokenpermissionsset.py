"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import processortokenpermissionssetresponse as shared_processortokenpermissionssetresponse
from typing import Optional


@dataclasses.dataclass
class ProcessorTokenPermissionsSetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    processor_token_permissions_set_response: Optional[shared_processortokenpermissionssetresponse.ProcessorTokenPermissionsSetResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

