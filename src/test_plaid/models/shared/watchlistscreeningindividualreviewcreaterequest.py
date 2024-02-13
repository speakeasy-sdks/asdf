"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WatchlistScreeningIndividualReviewCreateRequest:
    r"""Request input for creating a screening review"""
    UNSET='__SPEAKEASY_UNSET__'
    confirmed_hits: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confirmed_hits') }})
    r"""Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected."""
    dismissed_hits: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dismissed_hits') }})
    r"""Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed."""
    watchlist_screening_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('watchlist_screening_id') }})
    r"""ID of the associated screening."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    comment: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment'), 'exclude': lambda f: f is WatchlistScreeningIndividualReviewCreateRequest.UNSET }})
    r"""A comment submitted by a team member as part of reviewing a watchlist screening."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

