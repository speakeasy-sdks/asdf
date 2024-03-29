"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetReportCreateResponse:
    r"""AssetReportCreateResponse defines the response schema for `/asset_report/create`"""
    UNSET='__SPEAKEASY_UNSET__'
    asset_report_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('asset_report_id') }})
    r"""A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive."""
    asset_report_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('asset_report_token') }})
    r"""A token that can be provided to endpoints such as `/asset_report/get` or `/asset_report/pdf/get` to fetch or update an Asset Report."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

