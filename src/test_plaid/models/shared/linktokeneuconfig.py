"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LinkTokenEUConfig:
    r"""Configuration parameters for EU flows"""
    headless: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headless'), 'exclude': lambda f: f is None }})
    r"""If `true`, open Link without an initial UI. Defaults to `false`."""
    

