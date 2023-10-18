"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import creditfreddiemacloans_voa_2_4 as shared_creditfreddiemacloans_voa_2_4
from ..shared import creditfreddiemacparties_voa_2_4 as shared_creditfreddiemacparties_voa_2_4
from ..shared import creditfreddiemacservices_voa_2_4 as shared_creditfreddiemacservices_voa_2_4
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacVerificationOfAssetsDealVOA24:
    r"""An object representing an Asset Report with Freddie Mac schema."""
    loans: shared_creditfreddiemacloans_voa_2_4.CreditFreddieMacLoansVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('LOANS') }})
    r"""A collection of loans that are part of a single deal."""
    parties: shared_creditfreddiemacparties_voa_2_4.CreditFreddieMacPartiesVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('PARTIES') }})
    r"""A collection of objects that define specific parties to a deal. This includes the direct participating parties, such as borrower and seller and the indirect parties such as the credit report provider."""
    services: shared_creditfreddiemacservices_voa_2_4.CreditFreddieMacServicesVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SERVICES') }})
    r"""A collection of objects that describe requests and responses for services."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
