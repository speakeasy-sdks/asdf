"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from test_plaid import utils
from typing import Any, Dict, Optional

class EmailType(str, Enum):
    r"""The type of email account as described by the financial institution."""
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    OTHER = 'other'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Email:
    r"""An object representing an email address"""
    data: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    r"""The email address."""
    primary: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary') }})
    r"""When `true`, identifies the email address as the primary email on an account."""
    type: EmailType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of email account as described by the financial institution."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

