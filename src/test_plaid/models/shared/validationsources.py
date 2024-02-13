"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .validationsource import ValidationSource
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ValidationSources:
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    UNSET='__SPEAKEASY_UNSET__'
    validation_source: List[ValidationSource] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VALIDATION_SOURCE') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

