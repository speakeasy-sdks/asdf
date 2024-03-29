"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .recurringfrequency import RecurringFrequency
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Recurrence:
    r"""Insights relating to expenses and deposits that are predicted to occur on a scheduled basis, such as biweekly, monthly, or annually.

    Common examples include loan payments, bill payments, subscriptions, and payroll income.

    This is a beta field, available to all users.
    """
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    frequency: Optional[RecurringFrequency] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency'), 'exclude': lambda f: f is Recurrence.UNSET }})
    r"""Describes the frequency of the transaction stream.

    `WEEKLY`: Assigned to a transaction stream that occurs approximately every week.

    `BIWEEKLY`: Assigned to a transaction stream that occurs approximately every 2 weeks.

    `SEMI_MONTHLY`: Assigned to a transaction stream that occurs approximately twice per month. This frequency is typically seen for inflow transaction streams.

    `MONTHLY`: Assigned to a transaction stream that occurs approximately every month.

    `ANNUALLY`: Assigned to a transaction stream that occurs approximately every year.

    `DAILY`: Assigned to a transaction stream that occurs approximately every day.

    `DYNAMIC`: Assigned to a transaction stream that varies in recurrence frequency. This frequency is typically seen for inflow streams in the gig economy. 

    `UNKNOWN`: Assigned to a transaction stream that isn't recurring in nature.
    """
    is_recurring: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_recurring'), 'exclude': lambda f: f is Recurrence.UNSET }})
    r"""Whether or not the transaction is periodically recurring."""
    

