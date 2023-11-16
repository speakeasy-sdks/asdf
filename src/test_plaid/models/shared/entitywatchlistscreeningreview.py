"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .watchlistscreeningaudittrail import WatchlistScreeningAuditTrail
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityWatchlistScreeningReview:
    r"""A review submitted by a team member for an entity watchlist screening. A review can be either a comment on the current screening state, actions taken
    against hits attached to the watchlist screening, or both.
    """
    audit_trail: WatchlistScreeningAuditTrail = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audit_trail') }})
    r"""Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""
    comment: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment') }})
    r"""A comment submitted by a team member as part of reviewing a watchlist screening."""
    confirmed_hits: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confirmed_hits') }})
    r"""Hits marked as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected."""
    dismissed_hits: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dismissed_hits') }})
    r"""Hits marked as a false positive after thorough manual review. These hits will never recur or be updated once dismissed."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""ID of the associated entity review."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

