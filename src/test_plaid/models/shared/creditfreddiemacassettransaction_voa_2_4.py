"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .assettransactiondescription import AssetTransactionDescription
from .assettransactiondetail import AssetTransactionDetail
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacAssetTransactionVOA24:
    r"""An object representing..."""
    asset_transaction_description: List[AssetTransactionDescription] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_TRANSACTION_DESCRIPTION') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    asset_transaction_detail: AssetTransactionDetail = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_TRANSACTION_DETAIL') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

