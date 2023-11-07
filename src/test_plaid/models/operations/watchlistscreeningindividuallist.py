"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import watchlistscreeningindividuallistresponse as shared_watchlistscreeningindividuallistresponse
from typing import Optional


@dataclasses.dataclass
class WatchlistScreeningIndividualListResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    watchlist_screening_individual_list_response: Optional[shared_watchlistscreeningindividuallistresponse.WatchlistScreeningIndividualListResponse] = dataclasses.field(default=None)
    r"""OK"""
    

