"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .beaconusercreateembeddedreport import BeaconUserCreateEmbeddedReport
from .beaconuserrequestdata import BeaconUserRequestData
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BeaconUserCreateRequest:
    r"""Request input for creating a Beacon User.

    The primary use for this endpoint is to add a new end user to Beacon for fraud and duplicate scanning.
    This endpoint can also be used to import historical fraud cases into the Beacon Network without being charged
    for creating a Beacon User. To import historical fraud cases, embed the fraud report in the optional `report`
    section of the request payload.
    """
    UNSET='__SPEAKEASY_UNSET__'
    client_user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_user_id') }})
    r"""A unique ID that identifies the end user in your system. This ID can also be used to associate user-specific data from other Plaid products. Financial Account Matching requires this field and the `/link/token/create` `client_user_id` to be consistent. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`."""
    program_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('program_id') }})
    r"""ID of the associated Beacon Program."""
    user: BeaconUserRequestData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""A Beacon User's data which is used to check against duplicate records and the Beacon Fraud Network."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    report: Optional[BeaconUserCreateEmbeddedReport] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('report'), 'exclude': lambda f: f is BeaconUserCreateRequest.UNSET }})
    r"""Data for creating a Beacon Report as part of an initial Beacon User creation. Providing a fraud report as part of an initial Beacon User creation will omit the Beacon User from any billing charges."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

