"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import credit1099filer as shared_credit1099filer
from ..shared import credit1099payer as shared_credit1099payer
from ..shared import credit1099recipient as shared_credit1099recipient
from ..shared import creditdocumentmetadata as shared_creditdocumentmetadata
from ..shared import form1099type as shared_form1099type
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Credit1099:
    r"""An object representing an end user's 1099 tax form"""
    document_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_id') }})
    r"""An identifier of the document referenced by the document metadata."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    april_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('april_amount') }})
    r"""Amount reported for April."""
    august_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('august_amount') }})
    r"""Amount reported for August."""
    card_not_present_transaction: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_not_present_transaction') }})
    r"""Amount in card not present transactions."""
    crop_insurance_proceeds: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('crop_insurance_proceeds') }})
    r"""Amount of crop insurance proceeds."""
    december_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('december_amount') }})
    r"""Amount reported for December."""
    document_metadata: Optional[shared_creditdocumentmetadata.CreditDocumentMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_metadata'), 'exclude': lambda f: f is None }})
    r"""Object representing metadata pertaining to the document."""
    excess_golden_parachute_payments: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excess_golden_parachute_payments') }})
    r"""Amount of golden parachute payments made by payer."""
    february_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('february_amount') }})
    r"""Amount reported for February."""
    federal_income_tax_withheld: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('federal_income_tax_withheld') }})
    r"""Amount of federal income tax withheld from payer."""
    filer: Optional[shared_credit1099filer.Credit1099Filer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filer'), 'exclude': lambda f: f is None }})
    r"""An object representing a filer used by 1099-K tax documents."""
    fishing_boat_proceeds: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fishing_boat_proceeds') }})
    r"""Amount of fishing boat proceeds from payer."""
    form_1099_type: Optional[shared_form1099type.Form1099Type] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('form_1099_type'), 'exclude': lambda f: f is None }})
    r"""Form 1099 Type"""
    gross_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gross_amount') }})
    r"""Gross amount reported."""
    gross_proceeds_paid_to_an_attorney: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gross_proceeds_paid_to_an_attorney') }})
    r"""Amount of gross proceeds paid to an attorney by payer."""
    january_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('january_amount') }})
    r"""Amount reported for January."""
    july_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('july_amount') }})
    r"""Amount reported for July."""
    june_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('june_amount') }})
    r"""Amount reported for June."""
    march_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('march_amount') }})
    r"""Amount reported for March."""
    may_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('may_amount') }})
    r"""Amount reported for May."""
    medical_and_healthcare_payments: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('medical_and_healthcare_payments') }})
    r"""Amount of medical and healthcare payments from payer."""
    merchant_category_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_category_code') }})
    r"""Merchant category of filer."""
    nonemployee_compensation: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nonemployee_compensation') }})
    r"""Amount of nonemployee compensation from payer."""
    november_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('november_amount') }})
    r"""Amount reported for November."""
    number_of_payment_transactions: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number_of_payment_transactions') }})
    r"""Number of payment transactions made."""
    october_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('october_amount') }})
    r"""Amount reported for October."""
    other_income: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('other_income') }})
    r"""Amount in other income by payer."""
    payer: Optional[shared_credit1099payer.Credit1099Payer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payer'), 'exclude': lambda f: f is None }})
    r"""An object representing a payer used by 1099-MISC tax documents."""
    payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer') }})
    r"""Whether or not payer made direct sales over $5000 of consumer products."""
    payer_state_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payer_state_number') }})
    r"""Primary state ID."""
    payer_state_number_lower: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payer_state_number_lower') }})
    r"""Secondary state ID."""
    primary_state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary_state') }})
    r"""Primary state of business."""
    primary_state_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary_state_id') }})
    r"""Primary state ID."""
    primary_state_income_tax: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary_state_income_tax') }})
    r"""State income tax reported for primary state."""
    pse_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pse_name') }})
    r"""Name of the PSE (Payment Settlement Entity)."""
    pse_telephone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pse_telephone_number') }})
    r"""Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity)."""
    recipient: Optional[shared_credit1099recipient.Credit1099Recipient] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient'), 'exclude': lambda f: f is None }})
    r"""An object representing a recipient used in both 1099-K and 1099-MISC tax documents."""
    rents: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rents') }})
    r"""Amount in rent by payer."""
    royalties: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('royalties') }})
    r"""Amount in royalties by payer."""
    secondary_state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secondary_state') }})
    r"""Secondary state of business."""
    secondary_state_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secondary_state_id') }})
    r"""Secondary state ID."""
    secondary_state_income_tax: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secondary_state_income_tax') }})
    r"""State income tax reported for secondary state."""
    section_409a_deferrals: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('section_409a_deferrals') }})
    r"""Amount of 409A deferrals earned by payer."""
    section_409a_income: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('section_409a_income') }})
    r"""Amount of 409A income earned by payer."""
    september_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('september_amount') }})
    r"""Amount reported for September."""
    state_income: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state_income') }})
    r"""State income reported for primary state."""
    state_income_lower: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state_income_lower') }})
    r"""State income reported for secondary state."""
    state_tax_withheld: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state_tax_withheld') }})
    r"""Amount of state tax withheld of payer for primary state."""
    state_tax_withheld_lower: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state_tax_withheld_lower') }})
    r"""Amount of state tax withheld of payer for secondary state."""
    substitute_payments_in_lieu_of_dividends_or_interest: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('substitute_payments_in_lieu_of_dividends_or_interest') }})
    r"""Amount of substitute payments made by payer."""
    tax_year: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_year') }})
    r"""Tax year of the tax form."""
    transactions_reported: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions_reported') }})
    r"""One of the values will be provided Payment card Third party network"""
    

