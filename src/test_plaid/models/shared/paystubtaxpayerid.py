"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayStubTaxpayerID:
    r"""Taxpayer ID of the individual receiving the paystub."""
    UNSET='__SPEAKEASY_UNSET__'
    id_mask: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id_mask') }})
    r"""ID mask; i.e. last 4 digits of the taxpayer ID."""
    id_type: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id_type') }})
    r"""Type of ID, e.g. 'SSN'."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

