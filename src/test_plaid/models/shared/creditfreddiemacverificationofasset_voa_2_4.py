"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfreddiemacreportinginformation_voa_2_4 import CreditFreddieMacReportingInformationVOA24
from .creditfreddiemacverificationofassetresponse_voa_2_4 import CreditFreddieMacVerificationOfAssetResponseVOA24
from .serviceproductfulfillment import ServiceProductFulfillment
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacVerificationOfAssetVOA24:
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    UNSET='__SPEAKEASY_UNSET__'
    reporting_information: CreditFreddieMacReportingInformationVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('REPORTING_INFORMATION') }})
    r"""Information about an report identifier and a report name."""
    service_product_fulfillment: ServiceProductFulfillment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SERVICE_PRODUCT_FULFILLMENT') }})
    r"""A collection of details related to a fulfillment service or product in terms of request, process and result."""
    verification_of_asset_response: CreditFreddieMacVerificationOfAssetResponseVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VERIFICATION_OF_ASSET_RESPONSE') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

