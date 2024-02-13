"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .entitywatchlistscreeningsearchterms import EntityWatchlistScreeningSearchTerms
from .watchlistscreeningaudittrail import WatchlistScreeningAuditTrail
from .watchlistscreeningstatus import WatchlistScreeningStatus
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WatchlistScreeningEntityGetResponse:
    r"""The entity screening object allows you to represent an entity in your system, update its profile, and search for it on various watchlists. Note: Rejected entity screenings will not receive new hits, regardless of entity program configuration."""
    UNSET='__SPEAKEASY_UNSET__'
    assignee: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignee') }})
    r"""ID of the associated user."""
    audit_trail: WatchlistScreeningAuditTrail = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audit_trail') }})
    r"""Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""
    client_user_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_user_id') }})
    r"""A unique ID that identifies the end user in your system. This ID can also be used to associate user-specific data from other Plaid products. Financial Account Matching requires this field and the `/link/token/create` `client_user_id` to be consistent. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""ID of the associated entity screening."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    search_terms: EntityWatchlistScreeningSearchTerms = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_terms') }})
    r"""Search terms associated with an entity used for searching against watchlists"""
    status: WatchlistScreeningStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""A status enum indicating whether a screening is still pending review, has been rejected, or has been cleared."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

