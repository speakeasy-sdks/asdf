"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import identityverification as shared_identityverification
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IdentityVerificationListResponse:
    r"""Paginated list of Plaid sessions."""
    identity_verifications: List[shared_identityverification.IdentityVerification] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identity_verifications') }})
    r"""List of Plaid sessions"""
    next_cursor: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_cursor') }})
    r"""An identifier that determines which page of results you receive."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

