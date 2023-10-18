"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class DepositoryAccountSubtype(str, Enum):
    r"""Valid account subtypes for depository accounts. For a list containing descriptions of each subtype, see [Account schemas](https://plaid.com/docs/api/accounts/#StandaloneAccountType-depository)."""
    CHECKING = 'checking'
    SAVINGS = 'savings'
    HSA = 'hsa'
    CD = 'cd'
    MONEY_MARKET = 'money market'
    PAYPAL = 'paypal'
    PREPAID = 'prepaid'
    CASH_MANAGEMENT = 'cash management'
    EBT = 'ebt'
    ALL = 'all'