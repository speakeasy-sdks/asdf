"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import transferuseraddressinresponse as shared_transferuseraddressinresponse
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferUserInResponse:
    r"""The legal name and other information for the account holder."""
    address: Optional[shared_transferuseraddressinresponse.TransferUserAddressInResponse] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""The address associated with the account holder."""
    email_address: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_address') }})
    r"""The user's email address."""
    legal_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legal_name') }})
    r"""The user's legal name."""
    phone_number: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number') }})
    r"""The user's phone number."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
