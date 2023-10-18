"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import watchlistscreeningentityreviewcreateresponse as shared_watchlistscreeningentityreviewcreateresponse
from typing import Optional


@dataclasses.dataclass
class WatchlistScreeningEntityReviewCreateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    watchlist_screening_entity_review_create_response: Optional[shared_watchlistscreeningentityreviewcreateresponse.WatchlistScreeningEntityReviewCreateResponse] = dataclasses.field(default=None)
    r"""OK"""
    

