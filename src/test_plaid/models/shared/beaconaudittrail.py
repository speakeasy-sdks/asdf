"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .beaconaudittrailsource import BeaconAuditTrailSource
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BeaconAuditTrail:
    r"""Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""
    UNSET='__SPEAKEASY_UNSET__'
    dashboard_user_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dashboard_user_id') }})
    r"""ID of the associated user."""
    source: BeaconAuditTrailSource = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    r"""A type indicating what caused a resource to be changed or updated.


    `dashboard` - The resource was created or updated by a member of your team via the Plaid dashboard.

    `api` - The resource was created or updated via the Plaid API.

    `system` - The resource was created or updated automatically by a part of the Plaid Beacon system. For example, if another business using Plaid Beacon created a fraud report that matched one of your users, your matching user's status would automatically be updated and the audit trail source would be `system`.

    `bulk_import` - The resource was created or updated as part of a bulk import process. For example, if your company provided a CSV of user data as part of your initial onboarding, the audit trail source would be `bulk_import`.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

