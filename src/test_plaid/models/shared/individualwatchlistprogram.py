"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .individualwatchlistcode import IndividualWatchlistCode
from .programnamesensitivity import ProgramNameSensitivity
from .watchlistscreeningaudittrail import WatchlistScreeningAuditTrail
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IndividualWatchlistProgram:
    r"""A program that configures the active lists, search parameters, and other behavior for initial and ongoing screening of individuals."""
    UNSET='__SPEAKEASY_UNSET__'
    audit_trail: WatchlistScreeningAuditTrail = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audit_trail') }})
    r"""Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""ID of the associated program."""
    is_archived: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_archived') }})
    r"""Archived programs are read-only and cannot screen new customers nor participate in ongoing monitoring."""
    is_rescanning_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_rescanning_enabled') }})
    r"""Indicator specifying whether the program is enabled and will perform daily rescans."""
    lists_enabled: List[IndividualWatchlistCode] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lists_enabled') }})
    r"""Watchlists enabled for the associated program"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""A name for the program to define its purpose. For example, \\"High Risk Individuals\\", \\"US Cardholders\\", or \\"Applicants\\"."""
    name_sensitivity: ProgramNameSensitivity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name_sensitivity') }})
    r"""The valid name matching sensitivity configurations for a screening program. Note that while certain matching techniques may be more prevalent on less strict settings, all matching algorithms are enabled for every sensitivity.

    `coarse` - See more potential matches. This sensitivity will see more broad phonetic matches across alphabets that make missing a potential hit very unlikely. This setting is noisier and will require more manual review.

    `balanced` - A good default for most companies. This sensitivity is balanced to show high quality hits with reduced noise.

    `strict` - Aggressive false positive reduction. This sensitivity will require names to be more similar than `coarse` and `balanced` settings, relying less on phonetics, while still accounting for character transpositions, missing tokens, and other common permutations.

    `exact` - Matches must be nearly exact. This sensitivity will only show hits with exact or nearly exact name matches with only basic correction such as extraneous symbols and capitalization. This setting is generally not recommended unless you have a very specific use case.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

