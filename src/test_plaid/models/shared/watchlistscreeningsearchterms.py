"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WatchlistScreeningSearchTerms:
    r"""Search terms for creating an individual watchlist screening"""
    UNSET='__SPEAKEASY_UNSET__'
    country: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form."""
    date_of_birth: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_of_birth'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    document_number: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_number') }})
    r"""The numeric or alphanumeric identifier associated with this document."""
    legal_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legal_name') }})
    r"""The legal name of the individual being screened."""
    version: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version') }})
    r"""The current version of the search terms. Starts at `1` and increments with each edit to `search_terms`."""
    watchlist_program_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('watchlist_program_id') }})
    r"""ID of the associated program."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

