"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AssetReportPDFGetRequestOptions:
    r"""An optional object to filter or add data to `/asset_report/get` results. If provided, must be non-`null`."""
    days_to_include: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_to_include') }})
    r"""The maximum integer number of days of history to include in the Asset Report."""
    

