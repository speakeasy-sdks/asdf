"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import plaiderror as shared_plaiderror
from ..shared import processortransactionsrefreshresponse as shared_processortransactionsrefreshresponse
from typing import Optional


@dataclasses.dataclass
class ProcessorTransactionsRefreshResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    plaid_error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response"""
    processor_transactions_refresh_response: Optional[shared_processortransactionsrefreshresponse.ProcessorTransactionsRefreshResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

