"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import itemwebhookupdateresponse as shared_itemwebhookupdateresponse
from typing import Optional


@dataclasses.dataclass
class ItemWebhookUpdateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    item_webhook_update_response: Optional[shared_itemwebhookupdateresponse.ItemWebhookUpdateResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

