"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import watchlistscreeningindividual as shared_watchlistscreeningindividual
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WatchlistScreeningIndividualListResponse:
    r"""Paginated list of individual watchlist screenings."""
    next_cursor: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_cursor') }})
    r"""An identifier that determines which page of results you receive."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    watchlist_screenings: List[shared_watchlistscreeningindividual.WatchlistScreeningIndividual] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('watchlist_screenings') }})
    r"""List of individual watchlist screenings"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

