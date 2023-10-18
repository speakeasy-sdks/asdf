"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import scopesnullable as shared_scopesnullable
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectedApplication:
    r"""Describes the connected application for a particular end user."""
    application_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_id') }})
    r"""This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect."""
    created_at: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date this application was linked in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the application"""
    application_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_url') }})
    r"""The URL for the application's website"""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name') }})
    r"""A human-readable name of the application for display purposes"""
    logo_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo_url') }})
    r"""A URL that links to the application logo image."""
    reason_for_access: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason_for_access') }})
    r"""A string provided by the connected app stating why they use their respective enabled products."""
    scopes: Optional[shared_scopesnullable.ScopesNullable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scopes') }})
    r"""The scopes object"""
    

