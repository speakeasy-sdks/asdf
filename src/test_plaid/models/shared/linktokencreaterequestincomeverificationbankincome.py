"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LinkTokenCreateRequestIncomeVerificationBankIncome:
    r"""Specifies options for initializing Link for use with Bank Income. This field is required if `income_verification` is included in the `products` array and `bank` is specified in `income_source_types`."""
    days_requested: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_requested') }})
    r"""The number of days of data to request for the Bank Income product"""
    enable_multiple_items: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_multiple_items') }})
    r"""Whether to enable multiple Items to be added in the Link session"""
    

