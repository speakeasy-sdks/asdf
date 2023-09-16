"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LinkTokenCreateRequestEmploymentBankIncome:
    r"""Specifies options for initializing Link for use with Bank Employment. This field is required if `employment` is included in the `products` array and `bank` is specified in `employment_source_types`."""
    days_requested: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_requested') }})
    r"""The number of days of data to request for the Bank Employment product."""
    

