"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DateRange:
    r"""A date range with a start and end date"""
    UNSET='__SPEAKEASY_UNSET__'
    beginning: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('beginning'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    ending: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ending'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

