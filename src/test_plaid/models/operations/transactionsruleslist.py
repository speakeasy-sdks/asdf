"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import plaiderror as shared_plaiderror
from ...models.shared import transactionsruleslistresponse as shared_transactionsruleslistresponse
from typing import Optional


@dataclasses.dataclass
class TransactionsRulesListResponse:
    UNSET='__SPEAKEASY_UNSET__'
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    plaid_error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=UNSET)
    r"""Error response"""
    transactions_rules_list_response: Optional[shared_transactionsruleslistresponse.TransactionsRulesListResponse] = dataclasses.field(default=None)
    r"""OK"""
    

