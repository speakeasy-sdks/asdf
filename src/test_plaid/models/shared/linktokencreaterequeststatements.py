"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LinkTokenCreateRequestStatements:
    r"""Specifies options for initializing Link for use with the Statements product."""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The end date for statements, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) “YYYY-MM-DD” format, e.g. \\"2020-10-30\\". If no value is provided, this will default to the current date."""
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The start date for statements, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) “YYYY-MM-DD” format, e.g. \\"2020-10-30\\". If no value is provided, this will default to 3 months prior to the current date."""
    
