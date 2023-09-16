"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import assetreportcreaterequestoptions as shared_assetreportcreaterequestoptions
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AssetReportCreateRequest:
    r"""AssetReportCreateRequest defines the request schema for `/asset_report/create`"""
    days_requested: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_requested') }})
    r"""The maximum integer number of days of history to include in the Asset Report. If using Fannie Mae Day 1 Certainty, `days_requested` must be at least 61 for new originations or at least 31 for refinancings.

    An Asset Report requested with \"Additional History\" (that is, with more than 61 days of transaction history) will incur an Additional History fee.
    """
    access_tokens: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_tokens'), 'exclude': lambda f: f is None }})
    r"""An array of access tokens corresponding to the Items that will be included in the report. The `assets` product must have been initialized for the Items during link; the Assets product cannot be added after initialization."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    options: Optional[shared_assetreportcreaterequestoptions.AssetReportCreateRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""An optional object to filter `/asset_report/create` results. If provided, must be non-`null`. The optional `user` object is required for the report to be eligible for Fannie Mae's Day 1 Certainty program."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    user_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_token'), 'exclude': lambda f: f is None }})
    r"""The user token associated with the User for which to create an asset report for. All items associated with the User will be included in the report."""
    
