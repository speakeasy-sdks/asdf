"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .productstatusbreakdown import ProductStatusBreakdown
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from test_plaid import utils
from typing import Any, Dict, Optional

class ProductStatusStatus(str, Enum):
    r"""This field is deprecated in favor of the `breakdown` object, which provides more granular institution health data.

    `HEALTHY`: the majority of requests are successful
    `DEGRADED`: only some requests are successful
    `DOWN`: all requests are failing

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    HEALTHY = 'HEALTHY'
    DEGRADED = 'DEGRADED'
    DOWN = 'DOWN'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProductStatus:
    r"""A representation of the status health of a request type. Auth requests, Balance requests, Identity requests, Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item logins each have their own status object."""
    UNSET='__SPEAKEASY_UNSET__'
    breakdown: ProductStatusBreakdown = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('breakdown') }})
    r"""A detailed breakdown of the institution's performance for a request type. The values for `success`, `error_plaid`, and `error_institution` sum to 1. The time range used for calculating the breakdown may range from the most recent few minutes to the past six hours. In general, smaller institutions will show status that was calculated over a longer period of time. For Investment updates, which are refreshed less frequently, the period assessed may be 24 hours or more. For more details, see [Institution status details](https://plaid.com/docs/account/activity/#institution-status-details)."""
    last_status_change: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_status_change'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""[ISO 8601](https://wikipedia.org/wiki/ISO_8601) formatted timestamp of the last status change for the institution."""
    status: ProductStatusStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""This field is deprecated in favor of the `breakdown` object, which provides more granular institution health data.

    `HEALTHY`: the majority of requests are successful
    `DEGRADED`: only some requests are successful
    `DOWN`: all requests are failing

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

