"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class TransferBalanceType(str, Enum):
    r"""The type of balance.

    `prefunded_rtp_credits` - Your prefunded RTP credit balance with Plaid
    `prefunded_ach_credits` - Your prefunded ACH credit balance with Plaid
    """
    PREFUNDED_RTP_CREDITS = 'prefunded_rtp_credits'
    PREFUNDED_ACH_CREDITS = 'prefunded_ach_credits'
