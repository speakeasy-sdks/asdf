"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .updateentityscreeningrequestsearchterms import UpdateEntityScreeningRequestSearchTerms
from .watchlistscreeningentityupdaterequestresettablefield import WatchlistScreeningEntityUpdateRequestResettableField
from .watchlistscreeningstatus import WatchlistScreeningStatus
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WatchlistScreeningEntityUpdateRequest:
    r"""Request input for editing an entity watchlist screening"""
    entity_watchlist_screening_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_watchlist_screening_id') }})
    r"""ID of the associated entity screening."""
    assignee: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignee'), 'exclude': lambda f: f is None }})
    r"""ID of the associated user."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    client_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_user_id'), 'exclude': lambda f: f is None }})
    r"""A unique ID that identifies the end user in your system. This ID can also be used to associate user-specific data from other Plaid products. Financial Account Matching requires this field and the `/link/token/create` `client_user_id` to be consistent. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`."""
    reset_fields: Optional[List[WatchlistScreeningEntityUpdateRequestResettableField]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reset_fields') }})
    r"""A list of fields to reset back to null"""
    search_terms: Optional[UpdateEntityScreeningRequestSearchTerms] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_terms') }})
    r"""Search terms for editing an entity watchlist screening"""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    status: Optional[WatchlistScreeningStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""A status enum indicating whether a screening is still pending review, has been rejected, or has been cleared."""
    

