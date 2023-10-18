"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetReportAuditCopyCreateResponse:
    r"""AssetReportAuditCopyCreateResponse defines the response schema for `/asset_report/audit_copy/get`"""
    audit_copy_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audit_copy_token') }})
    r"""A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
