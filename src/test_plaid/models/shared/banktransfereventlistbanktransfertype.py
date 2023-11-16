"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class BankTransferEventListBankTransferType(str, Enum):
    r"""The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into your origination account; a `credit` indicates a transfer of money out of your origination account."""
    DEBIT = 'debit'
    CREDIT = 'credit'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'
