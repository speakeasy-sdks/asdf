"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .kyccheckaddresssummary import KYCCheckAddressSummary
from .kyccheckdateofbirthsummary import KYCCheckDateOfBirthSummary
from .kyccheckidnumbersummary import KYCCheckIDNumberSummary
from .kycchecknamesummary import KYCCheckNameSummary
from .kyccheckphonesummary import KYCCheckPhoneSummary
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class KYCCheckDetails:
    r"""Additional information for the `kyc_check` step. This field will be `null` unless `steps.kyc_check` has reached a terminal state of either `success` or `failed`."""
    address: KYCCheckAddressSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""Result summary object specifying how the `address` field matched."""
    date_of_birth: KYCCheckDateOfBirthSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_of_birth') }})
    r"""Result summary object specifying how the `date_of_birth` field matched."""
    id_number: KYCCheckIDNumberSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id_number') }})
    r"""Result summary object specifying how the `id_number` field matched."""
    name: KYCCheckNameSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Result summary object specifying how the `name` field matched."""
    phone_number: KYCCheckPhoneSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number') }})
    r"""Result summary object specifying how the `phone` field matched."""
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The outcome status for the associated Identity Verification attempt's `kyc_check` step. This field will always have the same value as `steps.kyc_check`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

