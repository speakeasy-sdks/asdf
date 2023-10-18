"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import role as shared_role
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Roles:
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    role: shared_role.Role = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ROLE') }})
    r"""ADocumentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
