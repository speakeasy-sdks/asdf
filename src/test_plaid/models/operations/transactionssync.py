"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import plaiderror as shared_plaiderror
from ..shared import transactionssyncresponse as shared_transactionssyncresponse
from typing import Optional


@dataclasses.dataclass
class TransactionsSyncResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    plaid_error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    transactions_sync_response: Optional[shared_transactionssyncresponse.TransactionsSyncResponse] = dataclasses.field(default=None)
    r"""OK"""
    

