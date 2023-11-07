"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .numbersachnullable import NumbersACHNullable
from .numbersbacsnullable import NumbersBACSNullable
from .numberseftnullable import NumbersEFTNullable
from .numbersinternationalnullable import NumbersInternationalNullable
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProcessorNumber:
    r"""An object containing identifying numbers used for making electronic transfers to and from the `account`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by the `account` for which auth data has been requested, a null value will be returned."""
    ach: Optional[NumbersACHNullable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ach') }})
    r"""Identifying information for transferring money to or from a US account via ACH or wire transfer."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    bacs: Optional[NumbersBACSNullable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bacs') }})
    r"""Identifying information for transferring money to or from a UK bank account via BACS."""
    eft: Optional[NumbersEFTNullable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eft') }})
    r"""Identifying information for transferring money to or from a Canadian bank account via EFT."""
    international: Optional[NumbersInternationalNullable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('international') }})
    r"""Identifying information for transferring money to or from an international bank account via wire transfer."""
    

