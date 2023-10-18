"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import actionstate as shared_actionstate
from ..shared import activitytype as shared_activitytype
from ..shared import scopesnullable as shared_scopesnullable
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Activity:
    r"""Describes a consent activity."""
    activity: shared_activitytype.ActivityType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('activity') }})
    r"""Types of consent activities"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""A unique identifier for the activity"""
    initiated_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initiated_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date this activity was initiated [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC."""
    initiator: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initiator') }})
    r"""Application ID of the client who initiated the activity."""
    state: shared_actionstate.ActionState = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    r"""Enum representing the state of the action/activity."""
    scopes: Optional[shared_scopesnullable.ScopesNullable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scopes') }})
    r"""The scopes object"""
    target_application_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_application_id'), 'exclude': lambda f: f is None }})
    r"""This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect."""
    
