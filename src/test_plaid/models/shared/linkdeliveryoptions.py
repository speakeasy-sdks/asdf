"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .linkdeliveryrecipient import LinkDeliveryRecipient
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkDeliveryOptions:
    r"""Optional metadata related to the Hosted Link session"""
    recipient: Optional[LinkDeliveryRecipient] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient'), 'exclude': lambda f: f is None }})
    r"""Metadata related to the recipient. If the information required to populate this field is not available, leave it blank."""
    

