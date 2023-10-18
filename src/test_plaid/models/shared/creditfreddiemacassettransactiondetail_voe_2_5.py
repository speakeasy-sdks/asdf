"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import assettransactioncategorytype as shared_assettransactioncategorytype
from ..shared import assettransactiontype as shared_assettransactiontype
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacAssetTransactionDetailVOE25:
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    asset_transaction_category_type: Optional[shared_assettransactioncategorytype.AssetTransactionCategoryType] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AssetTransactionCategoryType') }})
    r"""Asset Transaction Category Type Enumerated derived by Vendor."""
    asset_transaction_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AssetTransactionDate'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Asset Transaction Date."""
    asset_transaction_paid_by_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AssetTransactionPaidByName') }})
    r"""Populate with who did the transaction."""
    asset_transaction_paid_to_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AssetTransactionPaidToName') }})
    r"""Populate with for whom the transaction is done."""
    asset_transaction_post_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AssetTransactionPostDate'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Asset Transaction Post Date."""
    asset_transaction_type: shared_assettransactiontype.AssetTransactionType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AssetTransactionType') }})
    r"""Asset Transaction Type."""
    asset_transaction_type_additional_description: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AssetTransactionTypeAdditionalDescription') }})
    r"""FI Provided - examples are atm, cash, check, credit, debit, deposit, directDebit, directDeposit, dividend, fee, interest, other, payment, pointOfSale, repeatPayment, serviceCharge, transfer."""
    asset_transaction_unique_identifier: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AssetTransactionUniqueIdentifier') }})
    r"""A vendor created unique Identifier."""
    financial_institution_transaction_identifier: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('FinancialInstitutionTransactionIdentifier') }})
    r"""FI provided Transaction Identifier."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

