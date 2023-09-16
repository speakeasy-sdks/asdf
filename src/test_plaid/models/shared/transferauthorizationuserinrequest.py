"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import transferuseraddressinrequest as shared_transferuseraddressinrequest
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TransferAuthorizationUserInRequest:
    r"""The legal name and other information for the account holder."""
    legal_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legal_name') }})
    r"""The user's legal name."""
    address: Optional[shared_transferuseraddressinrequest.TransferUserAddressInRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""The address associated with the account holder. Providing this data will improve the likelihood that Plaid will be able to guarantee the transfer, if applicable."""
    email_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_address'), 'exclude': lambda f: f is None }})
    r"""The user's email address. In order to qualify for a guaranteed transfer, at least one of `phone_number` or `email_address` must be provided."""
    phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is None }})
    r"""The user's phone number. In order to qualify for a guaranteed transfer, at least one of `phone_number` or `email_address` must be provided."""
    

