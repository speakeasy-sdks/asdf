"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditSessionDocumentIncomeResult:
    r"""The details of a document income verification in Link"""
    num_bank_statements_uploaded: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_bank_statements_uploaded') }})
    r"""The number of bank statements uploaded by the user."""
    num_paystubs_uploaded: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_paystubs_uploaded') }})
    r"""The number of paystubs uploaded by the user."""
    num_w2s_uploaded: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_w2s_uploaded') }})
    r"""The number of w2s uploaded by the user."""
    

