"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class BankTransferDirection(str, Enum):
    r"""Indicates the direction of the transfer: `outbound` for API-initiated transfers, or `inbound` for payments received by the FBO account."""
    OUTBOUND = 'outbound'
    INBOUND = 'inbound'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'