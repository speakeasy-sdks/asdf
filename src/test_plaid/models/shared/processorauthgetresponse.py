"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountbase import AccountBase
from .processornumber import ProcessorNumber
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProcessorAuthGetResponse:
    r"""ProcessorAuthGetResponse defines the response schema for `/processor/auth/get`"""
    account: AccountBase = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account') }})
    r"""A single account at a financial institution."""
    numbers: ProcessorNumber = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numbers') }})
    r"""An object containing identifying numbers used for making electronic transfers to and from the `account`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by the `account` for which auth data has been requested, a null value will be returned."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

