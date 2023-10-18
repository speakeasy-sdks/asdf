"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import creditfreddiemacverificationofasset_voe_2_5 as shared_creditfreddiemacverificationofasset_voe_2_5
from ..shared import statuses as shared_statuses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacServiceVOE25:
    r"""A collection of details related to a fulfillment service or product in terms of request, process and result."""
    statuses: shared_statuses.Statuses = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('STATUSES') }})
    r"""A collection of STATUS containers."""
    verification_of_asset: List[shared_creditfreddiemacverificationofasset_voe_2_5.CreditFreddieMacVerificationOfAssetVOE25] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VERIFICATION_OF_ASSET') }})
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

