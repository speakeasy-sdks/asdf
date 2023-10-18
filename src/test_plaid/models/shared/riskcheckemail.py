"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import riskcheckemaildomainiscustom as shared_riskcheckemaildomainiscustom
from ..shared import riskcheckemaildomainisdisposable as shared_riskcheckemaildomainisdisposable
from ..shared import riskcheckemaildomainisfreeprovider as shared_riskcheckemaildomainisfreeprovider
from ..shared import riskcheckemailisdeliverablestatus as shared_riskcheckemailisdeliverablestatus
from ..shared import riskcheckemailtopleveldomainissuspicious as shared_riskcheckemailtopleveldomainissuspicious
from ..shared import riskchecklinkedservice as shared_riskchecklinkedservice
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RiskCheckEmail:
    r"""Result summary object specifying values for `email` attributes of risk check."""
    breach_count: Optional[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('breach_count') }})
    r"""Count of all known breaches of this email address if known."""
    domain_is_custom: shared_riskcheckemaildomainiscustom.RiskCheckEmailDomainIsCustom = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_is_custom') }})
    r"""Indicates whether the email address domain is custom if known, i.e. a company domain and not free or disposable."""
    domain_is_disposable: shared_riskcheckemaildomainisdisposable.RiskCheckEmailDomainIsDisposable = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_is_disposable') }})
    r"""Indicates whether the email domain is listed as disposable if known. Disposable domains are often used to create email addresses that are part of a fake set of user details."""
    domain_is_free_provider: shared_riskcheckemaildomainisfreeprovider.RiskCheckEmailDomainIsFreeProvider = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_is_free_provider') }})
    r"""Indicates whether the email address domain is a free provider such as Gmail or Hotmail if known."""
    domain_registered_at: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_registered_at'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    first_breached_at: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_breached_at'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    is_deliverable: shared_riskcheckemailisdeliverablestatus.RiskCheckEmailIsDeliverableStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_deliverable') }})
    r"""SMTP-MX check to confirm the email address exists if known."""
    last_breached_at: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_breached_at'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    linked_services: List[shared_riskchecklinkedservice.RiskCheckLinkedService] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('linked_services') }})
    r"""A list of online services where this email address has been detected to have accounts or other activity."""
    top_level_domain_is_suspicious: shared_riskcheckemailtopleveldomainissuspicious.RiskCheckEmailTopLevelDomainIsSuspicious = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_level_domain_is_suspicious') }})
    r"""Indicates whether the email address top level domain, which is the last part of the domain, is fraudulent or risky if known. In most cases, a suspicious top level domain is also associated with a disposable or high-risk domain."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
