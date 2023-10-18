"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxpayerID:
    r"""Taxpayer ID of the individual receiving the paystub."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    id_mask: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id_mask') }})
    r"""ID mask; i.e. last 4 digits of the taxpayer ID"""
    id_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id_type') }})
    r"""Type of ID, e.g. 'SSN'"""
    last_4_digits: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_4_digits') }})
    r"""Last 4 digits of unique number of ID.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    

