"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import plaiderror as shared_plaiderror
from ...models.shared import transferdiligencesubmitresponse as shared_transferdiligencesubmitresponse
from typing import Optional


@dataclasses.dataclass
class TransferDiligenceSubmitResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    plaid_error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response"""
    transfer_diligence_submit_response: Optional[shared_transferdiligencesubmitresponse.TransferDiligenceSubmitResponse] = dataclasses.field(default=None)
    r"""OK"""
    

