"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .linksessionexitmetadatainstitution import LinkSessionExitMetadataInstitution
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkSessionExitMetadata:
    r"""Displayed if a user exits Link without successfully linking an Item."""
    institution: Optional[LinkSessionExitMetadataInstitution] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution') }})
    r"""An institution object. If the Item was created via Same-Day micro-deposit verification, will be `null`."""
    link_session_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_session_id'), 'exclude': lambda f: f is None }})
    r"""A unique identifier associated with a user's actions and events through the Link flow. Include this identifier when opening a support ticket for faster turnaround."""
    request_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id'), 'exclude': lambda f: f is None }})
    r"""The request ID for the last request made by Link. This can be shared with Plaid Support to expedite investigation."""
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The point at which the user exited the Link flow. One of the following values."""
    

