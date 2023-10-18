"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import matchsummarycode as shared_matchsummarycode
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class KYCCheckPhoneSummary:
    r"""Result summary object specifying how the `phone` field matched."""
    area_code: shared_matchsummarycode.MatchSummaryCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('area_code') }})
    r"""An enum indicating the match type between data provided by user and data checked against an external data source.


    `match` indicates that the provided input data was a strong match against external data.

    `partial_match` indicates the data approximately matched against external data. For example, \"Knope\" vs. \"Knope-Wyatt\" for last name.

    `no_match` indicates that Plaid was able to perform a check against an external data source and it did not match the provided input data.

    `no_data` indicates that Plaid was unable to find external data to compare against the provided input data.

    `no_input` indicates that Plaid was unable to perform a check because no information was provided for this field by the end user.
    """
    summary: shared_matchsummarycode.MatchSummaryCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary') }})
    r"""An enum indicating the match type between data provided by user and data checked against an external data source.


    `match` indicates that the provided input data was a strong match against external data.

    `partial_match` indicates the data approximately matched against external data. For example, \"Knope\" vs. \"Knope-Wyatt\" for last name.

    `no_match` indicates that Plaid was able to perform a check against an external data source and it did not match the provided input data.

    `no_data` indicates that Plaid was unable to find external data to compare against the provided input data.

    `no_input` indicates that Plaid was unable to perform a check because no information was provided for this field by the end user.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

