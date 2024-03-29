"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IdentityVerificationTemplateReference:
    r"""The resource ID and version number of the template configuring the behavior of a given identity verification."""
    UNSET='__SPEAKEASY_UNSET__'
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""ID of the associated Identity Verification template."""
    version: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version') }})
    r"""Version of the associated Identity Verification template."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

