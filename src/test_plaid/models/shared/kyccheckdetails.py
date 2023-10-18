"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import kyccheckaddresssummary as shared_kyccheckaddresssummary
from ..shared import kyccheckdateofbirthsummary as shared_kyccheckdateofbirthsummary
from ..shared import kyccheckidnumbersummary as shared_kyccheckidnumbersummary
from ..shared import kycchecknamesummary as shared_kycchecknamesummary
from ..shared import kyccheckphonesummary as shared_kyccheckphonesummary
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class KYCCheckDetails:
    r"""Additional information for the `kyc_check` step. This field will be `null` unless `steps.kyc_check` has reached a terminal state of either `success` or `failed`."""
    address: shared_kyccheckaddresssummary.KYCCheckAddressSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""Result summary object specifying how the `address` field matched."""
    date_of_birth: shared_kyccheckdateofbirthsummary.KYCCheckDateOfBirthSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_of_birth') }})
    r"""Result summary object specifying how the `date_of_birth` field matched."""
    id_number: shared_kyccheckidnumbersummary.KYCCheckIDNumberSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id_number') }})
    r"""Result summary object specifying how the `id_number` field matched."""
    name: shared_kycchecknamesummary.KYCCheckNameSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Result summary object specifying how the `name` field matched."""
    phone_number: shared_kyccheckphonesummary.KYCCheckPhoneSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number') }})
    r"""Result summary object specifying how the `phone` field matched."""
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The outcome status for the associated Identity Verification attempt's `kyc_check` step. This field will always have the same value as `steps.kyc_check`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
