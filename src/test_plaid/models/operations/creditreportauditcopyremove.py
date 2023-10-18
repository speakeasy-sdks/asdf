"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import creditauditcopytokenremoveresponse as shared_creditauditcopytokenremoveresponse
from typing import Optional


@dataclasses.dataclass
class CreditReportAuditCopyRemoveResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    credit_audit_copy_token_remove_response: Optional[shared_creditauditcopytokenremoveresponse.CreditAuditCopyTokenRemoveResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

