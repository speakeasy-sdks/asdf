"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from test_plaid import utils
from typing import Any, Dict, Optional

class RefreshInterval(str, Enum):
    r"""The `refresh_interval` may be `DELAYED` or `STOPPED` even when the success rate is high. This value is only returned for Transactions status breakdowns."""
    NORMAL = 'NORMAL'
    DELAYED = 'DELAYED'
    STOPPED = 'STOPPED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProductStatusBreakdown:
    r"""A detailed breakdown of the institution's performance for a request type. The values for `success`, `error_plaid`, and `error_institution` sum to 1. The time range used for calculating the breakdown may range from the most recent few minutes to the past six hours. In general, smaller institutions will show status that was calculated over a longer period of time. For Investment updates, which are refreshed less frequently, the period assessed may be 24 hours or more. For more details, see [Institution status details](https://plaid.com/docs/account/activity/#institution-status-details)."""
    UNSET='__SPEAKEASY_UNSET__'
    error_institution: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_institution') }})
    r"""The percentage of logins that are failing due to an issue in the institution's system, expressed as a decimal."""
    error_plaid: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_plaid') }})
    r"""The percentage of logins that are failing due to an internal Plaid issue, expressed as a decimal."""
    success: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success') }})
    r"""The percentage of login attempts that are successful, expressed as a decimal."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    refresh_interval: Optional[RefreshInterval] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_interval'), 'exclude': lambda f: f is None }})
    r"""The `refresh_interval` may be `DELAYED` or `STOPPED` even when the success rate is high. This value is only returned for Transactions status breakdowns."""
    

