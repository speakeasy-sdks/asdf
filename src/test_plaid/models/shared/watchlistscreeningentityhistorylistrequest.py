"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WatchlistScreeningEntityHistoryListRequest:
    r"""Request input for listing changes to entity watchlist screenings"""
    UNSET='__SPEAKEASY_UNSET__'
    entity_watchlist_screening_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_watchlist_screening_id') }})
    r"""ID of the associated entity screening."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    cursor: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursor'), 'exclude': lambda f: f is WatchlistScreeningEntityHistoryListRequest.UNSET }})
    r"""An identifier that determines which page of results you receive."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

