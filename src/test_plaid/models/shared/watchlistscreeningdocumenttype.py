"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class WatchlistScreeningDocumentType(str, Enum):
    r"""The kind of official document represented by this object.

    `birth_certificate` - A certificate of birth

    `drivers_license` - A license to operate a motor vehicle

    `immigration_number` - Immigration or residence documents

    `military_id` - Identification issued by a military group

    `other` - Any document not covered by other categories

    `passport` - An official passport issue by a government

    `personal_identification` - Any generic personal identification that is not covered by other categories

    `ration_card` - Identification that entitles the holder to rations

    `ssn` - United States Social Security Number

    `student_id` - Identification issued by an educational institution

    `tax_id` - Identification issued for the purpose of collecting taxes

    `travel_document` - Visas, entry permits, refugee documents, etc.

    `voter_id` - Identification issued for the purpose of voting
    """
    BIRTH_CERTIFICATE = 'birth_certificate'
    DRIVERS_LICENSE = 'drivers_license'
    IMMIGRATION_NUMBER = 'immigration_number'
    MILITARY_ID = 'military_id'
    OTHER = 'other'
    PASSPORT = 'passport'
    PERSONAL_IDENTIFICATION = 'personal_identification'
    RATION_CARD = 'ration_card'
    SSN = 'ssn'
    STUDENT_ID = 'student_id'
    TAX_ID = 'tax_id'
    TRAVEL_DOCUMENT = 'travel_document'
    VOTER_ID = 'voter_id'
