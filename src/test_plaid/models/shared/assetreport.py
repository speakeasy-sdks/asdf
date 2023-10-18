"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import assetreportitem as shared_assetreportitem
from ..shared import assetreportuser as shared_assetreportuser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetReport:
    r"""An object representing an Asset Report"""
    asset_report_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('asset_report_id') }})
    r"""A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive."""
    client_report_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_report_id') }})
    r"""An identifier you determine and submit for the Asset Report."""
    date_generated: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_generated'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time when the Asset Report was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \\"2018-04-12T03:32:11Z\\")."""
    days_requested: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_requested') }})
    r"""The duration of transaction history you requested"""
    items: List[shared_assetreportitem.AssetReportItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    r"""Data returned by Plaid about each of the Items included in the Asset Report."""
    user: shared_assetreportuser.AssetReportUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""The user object allows you to provide additional information about the user to be appended to the Asset Report. All fields are optional. The `first_name`, `last_name`, and `ssn` fields are required if you would like the Report to be eligible for Fannie Mae’s Day 1 Certainty™ program."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

