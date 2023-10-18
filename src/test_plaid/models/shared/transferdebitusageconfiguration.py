"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import achclass as shared_achclass
from ..shared import originatorexpectedtransferfrequency as shared_originatorexpectedtransferfrequency
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferDebitUsageConfiguration:
    r"""Specifies the originator's expected usage of debits. For all dollar amounts, use a decimal string with two digits of precision e.g. \\"10.00\\". This field is required if the originator is expected to process debit transfers."""
    expected_average_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expected_average_amount') }})
    r"""The originator’s expected average amount per debit."""
    expected_frequency: shared_originatorexpectedtransferfrequency.OriginatorExpectedTransferFrequency = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expected_frequency') }})
    r"""The originator's expected transfer frequency."""
    expected_highest_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expected_highest_amount') }})
    r"""The originator’s expected highest amount for a single debit transfer."""
    expected_monthly_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expected_monthly_amount') }})
    r"""The originator’s monthly expected ACH debit processing amount for the next 6-12 months."""
    sec_codes: List[shared_achclass.ACHClass] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sec_codes') }})
    r"""Specifies the expected use cases for the originator’s debit transfers. This should be a list that contains one or more of the following codes:

    `\"ccd\"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    `\"ppd\"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment

    `\"tel\"` - Telephone-Initiated Entry

    `\"web\"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet
    """
    

