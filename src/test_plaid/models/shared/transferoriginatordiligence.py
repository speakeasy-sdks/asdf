"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .transfercreditusageconfiguration import TransferCreditUsageConfiguration
from .transferdebitusageconfiguration import TransferDebitUsageConfiguration
from .transferoriginatoraddress import TransferOriginatorAddress
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferOriginatorDiligence:
    r"""The diligence information for the originator."""
    UNSET='__SPEAKEASY_UNSET__'
    address: TransferOriginatorAddress = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""The originator's address."""
    dba: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dba') }})
    r"""The business name of the originator."""
    naics_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('naics_code') }})
    r"""The NAICS code of the originator."""
    tax_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_id') }})
    r"""The tax ID of the originator."""
    website: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('website') }})
    r"""The website of the originator."""
    credit_usage_configuration: Optional[TransferCreditUsageConfiguration] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_usage_configuration'), 'exclude': lambda f: f is TransferOriginatorDiligence.UNSET }})
    r"""Specifies the originator's expected usage of credits. For all dollar amounts, use a decimal string with two digits of precision e.g. \\"10.00\\". This field is required if the originator is expected to process credit transfers."""
    debit_usage_configuration: Optional[TransferDebitUsageConfiguration] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('debit_usage_configuration'), 'exclude': lambda f: f is TransferOriginatorDiligence.UNSET }})
    r"""Specifies the originator's expected usage of debits. For all dollar amounts, use a decimal string with two digits of precision e.g. \\"10.00\\". This field is required if the originator is expected to process debit transfers."""
    

