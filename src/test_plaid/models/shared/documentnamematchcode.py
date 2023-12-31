"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class DocumentNameMatchCode(str, Enum):
    r"""A match summary describing the cross comparison between the subject's name, extracted from the document image, and the name they separately provided to identity verification attempt."""
    MATCH = 'match'
    PARTIAL_MATCH = 'partial_match'
    NO_MATCH = 'no_match'
