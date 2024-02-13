"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .assetowner import AssetOwner
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetOwners:
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    UNSET='__SPEAKEASY_UNSET__'
    asset_owner: List[AssetOwner] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_OWNER') }})
    r"""Multiple Occurances of Account Owners Full Name up to 4."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

