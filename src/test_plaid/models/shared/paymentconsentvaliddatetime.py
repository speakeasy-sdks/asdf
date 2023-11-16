"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentConsentValidDateTime:
    r"""Life span for the payment consent. After the `to` date the payment consent expires and can no longer be used for payment initiation."""
    from_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time from which the consent should be active, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    to: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time at which the consent expires, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    

