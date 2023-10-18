"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import taxpayeridentifier as shared_taxpayeridentifier
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxpayerIdentifiers:
    r"""The collection of TAXPAYER_IDENTIFICATION elements"""
    taxpayer_identifier: shared_taxpayeridentifier.TaxpayerIdentifier = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TAXPAYER_IDENTIFIER') }})
    r"""Information about the Taxpayer identification values assigned to the individual or legal entity.Information about the Taxpayer identification values assigned to the individual or legal entity."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
