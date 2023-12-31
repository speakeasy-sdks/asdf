"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class PartnerEndCustomerOAuthInstitutionApplicationStatus(str, Enum):
    r"""The registration status for the end customer's application."""
    NOT_STARTED = 'NOT_STARTED'
    PROCESSING = 'PROCESSING'
    APPROVED = 'APPROVED'
    ENABLED = 'ENABLED'
    ATTENTION_REQUIRED = 'ATTENTION_REQUIRED'
