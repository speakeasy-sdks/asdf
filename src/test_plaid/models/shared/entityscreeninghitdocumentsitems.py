"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import entitydocument as shared_entitydocument
from ..shared import matchsummary as shared_matchsummary
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityScreeningHitDocumentsItems:
    r"""Analyzed documents for the associated hit"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    analysis: Optional[shared_matchsummary.MatchSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('analysis'), 'exclude': lambda f: f is None }})
    r"""Summary object reflecting the match result of the associated data"""
    data: Optional[shared_entitydocument.EntityDocument] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""An official document, usually issued by a governing body or institution, with an associated identifier."""
    

