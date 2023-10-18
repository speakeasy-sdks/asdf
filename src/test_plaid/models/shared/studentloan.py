"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import pslfstatus as shared_pslfstatus
from ..shared import serviceraddressdata as shared_serviceraddressdata
from ..shared import studentloanstatus as shared_studentloanstatus
from ..shared import studentrepaymentplan as shared_studentrepaymentplan
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StudentLoan:
    r"""Contains details about a student loan account"""
    account_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The ID of the account that this liability belongs to."""
    account_number: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_number') }})
    r"""The account number of the loan. For some institutions, this may be a masked version of the number (e.g., the last 4 digits instead of the entire number)."""
    disbursement_dates: Optional[List[date]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disbursement_dates'), 'encoder': utils.list_encoder(False, utils.dateisoformat(False)), 'decoder': utils.list_decoder(utils.datefromisoformat) }})
    r"""The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    expected_payoff_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expected_payoff_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    guarantor: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('guarantor') }})
    r"""The guarantor of the student loan."""
    interest_rate_percentage: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interest_rate_percentage') }})
    r"""The interest rate on the loan as a percentage."""
    is_overdue: Optional[bool] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_overdue') }})
    r"""`true` if a payment is currently overdue. Availability for this field is limited."""
    last_payment_amount: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_payment_amount') }})
    r"""The amount of the last payment."""
    last_payment_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_payment_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    last_statement_issue_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_statement_issue_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    loan_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loan_name') }})
    r"""The type of loan, e.g., \\"Consolidation Loans\\"."""
    loan_status: shared_studentloanstatus.StudentLoanStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loan_status') }})
    r"""An object representing the status of the student loan"""
    minimum_payment_amount: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_payment_amount') }})
    r"""The minimum payment due for the next billing cycle. There are some exceptions:
    Some institutions require a minimum payment across all loans associated with an account number. Our API presents that same minimum payment amount on each loan. The institutions that do this are: Great Lakes ( `ins_116861`), Firstmark (`ins_116295`), Commonbond Firstmark Services (`ins_116950`), Nelnet (`ins_116528`), EdFinancial Services (`ins_116304`), Granite State (`ins_116308`), and Oklahoma Student Loan Authority (`ins_116945`).
    Firstmark (`ins_116295` ) and Navient (`ins_116248`) will display as $0 if there is an autopay program in effect.
    """
    next_payment_due_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_payment_due_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The due date for the next payment. The due date is `null` if a payment is not expected. A payment is not expected if `loan_status.type` is `deferment`, `in_school`, `consolidated`, `paid in full`, or `transferred`. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    origination_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    origination_principal_amount: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_principal_amount') }})
    r"""The original principal balance of the loan."""
    outstanding_interest_amount: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outstanding_interest_amount') }})
    r"""The total dollar amount of the accrued interest balance. For Sallie Mae ( `ins_116944`), this amount is included in the current balance of the loan, so this field will return as `null`."""
    payment_reference_number: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_reference_number') }})
    r"""The relevant account number that should be used to reference this loan for payments. In the majority of cases, `payment_reference_number` will match `account_number,` but in some institutions, such as Great Lakes (`ins_116861`), it will be different."""
    pslf_status: shared_pslfstatus.PSLFStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pslf_status') }})
    r"""Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is FedLoan (`ins_116527`)."""
    repayment_plan: shared_studentrepaymentplan.StudentRepaymentPlan = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('repayment_plan') }})
    r"""An object representing the repayment plan for the student loan"""
    sequence_number: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sequence_number') }})
    r"""The sequence number of the student loan. Heartland ECSI (`ins_116948`) does not make this field available."""
    servicer_address: shared_serviceraddressdata.ServicerAddressData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servicer_address') }})
    r"""The address of the student loan servicer. This is generally the remittance address to which payments should be sent."""
    ytd_interest_paid: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ytd_interest_paid') }})
    r"""The year to date (YTD) interest paid. Availability for this field is limited."""
    ytd_principal_paid: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ytd_principal_paid') }})
    r"""The year to date (YTD) principal paid. Availability for this field is limited."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
