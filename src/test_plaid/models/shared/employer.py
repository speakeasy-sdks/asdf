"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .addressdatanullable import AddressDataNullable
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Employer:
    r"""Data about the employer."""
    address: Optional[AddressDataNullable] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""Data about the components comprising an address."""
    confidence_score: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confidence_score') }})
    r"""A number from 0 to 1 indicating Plaid's level of confidence in the pairing between the employer and the institution (not yet implemented)."""
    employer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employer_id') }})
    r"""Plaid's unique identifier for the employer."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the employer"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

