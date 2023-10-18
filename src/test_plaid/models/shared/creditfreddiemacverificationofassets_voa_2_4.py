"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import creditfreddiemacverificationofassetsdeal_voa_2_4 as shared_creditfreddiemacverificationofassetsdeal_voa_2_4
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacVerificationOfAssetsVOA24:
    r"""Verification of Assets Report"""
    deal: shared_creditfreddiemacverificationofassetsdeal_voa_2_4.CreditFreddieMacVerificationOfAssetsDealVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DEAL') }})
    r"""An object representing an Asset Report with Freddie Mac schema."""
    schema_version: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SchemaVersion') }})
    r"""The Verification Of Assets (VOA) schema version."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

