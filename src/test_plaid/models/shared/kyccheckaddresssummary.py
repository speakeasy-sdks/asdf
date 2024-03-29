"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .addresspurposelabel import AddressPurposeLabel
from .matchsummarycode import MatchSummaryCode
from .poboxstatus import POBoxStatus
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class KYCCheckAddressSummary:
    r"""Result summary object specifying how the `address` field matched."""
    UNSET='__SPEAKEASY_UNSET__'
    po_box: POBoxStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('po_box') }})
    r"""Field describing whether the associated address is a post office box. Will be `yes` when a P.O. box is detected, `no` when Plaid confirmed the address is not a P.O. box, and `no_data` when Plaid was not able to determine if the address is a P.O. box."""
    summary: MatchSummaryCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary') }})
    r"""An enum indicating the match type between data provided by user and data checked against an external data source.


    `match` indicates that the provided input data was a strong match against external data.

    `partial_match` indicates the data approximately matched against external data. For example, \"Knope\" vs. \"Knope-Wyatt\" for last name.

    `no_match` indicates that Plaid was able to perform a check against an external data source and it did not match the provided input data.

    `no_data` indicates that Plaid was unable to find external data to compare against the provided input data.

    `no_input` indicates that Plaid was unable to perform a check because no information was provided for this field by the end user.
    """
    type: AddressPurposeLabel = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Field describing whether the associated address is being used for commercial or residential purposes.

    Note: This value will be `no_data` when Plaid does not have sufficient data to determine the address's use.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

