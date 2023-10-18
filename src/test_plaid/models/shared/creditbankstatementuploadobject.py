"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import creditbankstatementuploadbankaccount as shared_creditbankstatementuploadbankaccount
from ..shared import creditbankstatementuploadtransaction as shared_creditbankstatementuploadtransaction
from ..shared import creditdocumentmetadata as shared_creditdocumentmetadata
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankStatementUploadObject:
    r"""An object containing data that has been parsed from a user-uploaded bank statement."""
    bank_accounts: List[shared_creditbankstatementuploadbankaccount.CreditBankStatementUploadBankAccount] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_accounts') }})
    r"""An array of bank accounts associated with the uploaded bank statement."""
    document_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_id') }})
    r"""An identifier of the document referenced by the document metadata."""
    document_metadata: shared_creditdocumentmetadata.CreditDocumentMetadata = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_metadata') }})
    r"""Object representing metadata pertaining to the document."""
    transactions: List[shared_creditbankstatementuploadtransaction.CreditBankStatementUploadTransaction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions') }})
    r"""An array of transactions appearing on the bank statement."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
