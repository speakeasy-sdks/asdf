"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import assetdetail as shared_assetdetail
from ..shared import assetholder as shared_assetholder
from ..shared import assetowners as shared_assetowners
from ..shared import creditfreddiemacassettransactions_voa_2_4 as shared_creditfreddiemacassettransactions_voa_2_4
from ..shared import validationsources as shared_validationsources
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacAssetVOA24:
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    asset_detail: shared_assetdetail.AssetDetail = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_DETAIL') }})
    r"""Details about an asset."""
    asset_holder: shared_assetholder.AssetHolder = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_HOLDER') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    asset_owners: shared_assetowners.AssetOwners = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_OWNERS') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    asset_transactions: shared_creditfreddiemacassettransactions_voa_2_4.CreditFreddieMacAssetTransactionsVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_TRANSACTIONS') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    validation_sources: shared_validationsources.ValidationSources = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VALIDATION_SOURCES') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
