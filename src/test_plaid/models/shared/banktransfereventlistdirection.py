"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class BankTransferEventListDirection(str, Enum):
    r"""Indicates the direction of the transfer: `outbound`: for API-initiated transfers
    `inbound`: for payments received by the FBO account.
    """
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'
