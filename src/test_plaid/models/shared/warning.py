"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import cause as shared_cause
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from test_plaid import utils
from typing import Any, Dict, Optional

class WarningWarningCode(str, Enum):
    r"""The warning code identifies a specific kind of warning. `OWNERS_UNAVAILABLE` indicates that account-owner information is not available.`INVESTMENTS_UNAVAILABLE` indicates that Investments specific information is not available. `TRANSACTIONS_UNAVAILABLE` indicates that transactions information associated with Credit and Depository accounts are unavailable."""
    OWNERS_UNAVAILABLE = 'OWNERS_UNAVAILABLE'
    INVESTMENTS_UNAVAILABLE = 'INVESTMENTS_UNAVAILABLE'
    TRANSACTIONS_UNAVAILABLE = 'TRANSACTIONS_UNAVAILABLE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WarningT:
    r"""It is possible for an Asset Report to be returned with missing account owner information. In such cases, the Asset Report will contain warning data in the response, indicating why obtaining the owner information failed."""
    cause: Optional[shared_cause.Cause] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cause') }})
    r"""An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items."""
    warning_code: WarningWarningCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warning_code') }})
    r"""The warning code identifies a specific kind of warning. `OWNERS_UNAVAILABLE` indicates that account-owner information is not available.`INVESTMENTS_UNAVAILABLE` indicates that Investments specific information is not available. `TRANSACTIONS_UNAVAILABLE` indicates that transactions information associated with Credit and Depository accounts are unavailable."""
    warning_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warning_type') }})
    r"""The warning type, which will always be `ASSET_REPORT_WARNING`"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
