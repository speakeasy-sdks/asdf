"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .beaconuseridnumber import BeaconUserIDNumber
from .beaconusername import BeaconUserName
from .beaconuserrequestaddress import BeaconUserRequestAddress
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BeaconUserRequestData:
    r"""A Beacon User's data which is used to check against duplicate records and the Beacon Fraud Network."""
    UNSET='__SPEAKEASY_UNSET__'
    address: BeaconUserRequestAddress = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""Home address for the associated user. For more context on this field, see [Input Validation by Country](https://plaid.com/docs/identity-verification/hybrid-input-validation/#input-validation-by-country)."""
    date_of_birth: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_of_birth'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    name: BeaconUserName = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The full name for a given Beacon User."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    email_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_address'), 'exclude': lambda f: f is None }})
    r"""A valid email address."""
    id_number: Optional[BeaconUserIDNumber] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id_number'), 'exclude': lambda f: f is None }})
    r"""The ID number associated with a Beacon User."""
    ip_address: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ip_address'), 'exclude': lambda f: f is BeaconUserRequestData.UNSET }})
    r"""An IPv4 or IPV6 address."""
    phone_number: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is BeaconUserRequestData.UNSET }})
    r"""A phone number in E.164 format."""
    

