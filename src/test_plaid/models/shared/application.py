"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Application:
    r"""Metadata about the application"""
    application_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_id') }})
    r"""This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect."""
    application_url: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_url') }})
    r"""The URL for the application's website"""
    city: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    r"""A string representing the city of the client’s headquarters."""
    company_legal_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_legal_name') }})
    r"""A string representing the name of client’s legal entity."""
    country_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_code') }})
    r"""A string representing the country code of the client’s headquarters."""
    display_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name') }})
    r"""A human-readable name of the application for display purposes"""
    join_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date this application was granted production access at Plaid in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC."""
    logo_url: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo_url') }})
    r"""A URL that links to the application logo image."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the application"""
    postal_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code') }})
    r"""A string representing the postal code of the client’s headquarters."""
    reason_for_access: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason_for_access') }})
    r"""A string provided by the connected app stating why they use their respective enabled products."""
    region: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""A string representing the region of the client’s headquarters."""
    use_case: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('use_case') }})
    r"""A string representing client’s broad use case as assessed by Plaid."""
    
