"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditpaystubaddress import CreditPayStubAddress
from .paystubtaxpayerid import PayStubTaxpayerID
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditPayStubEmployee:
    r"""Data about the employee."""
    UNSET='__SPEAKEASY_UNSET__'
    address: CreditPayStubAddress = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""Address on the pay stub."""
    marital_status: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('marital_status') }})
    r"""Marital status of the employee - either `SINGLE` or `MARRIED`."""
    name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the employee."""
    taxpayer_id: PayStubTaxpayerID = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxpayer_id') }})
    r"""Taxpayer ID of the individual receiving the paystub."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

