"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .riskcheckstolenidentity import RiskCheckStolenIdentity
from .riskchecksyntheticidentity import RiskCheckSyntheticIdentity
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RiskCheckIdentityAbuseSignals:
    r"""Result summary object capturing abuse signals related to `identity abuse`, e.g. stolen and synthetic identity fraud."""
    stolen_identity: Optional[RiskCheckStolenIdentity] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stolen_identity') }})
    r"""Field containing the data used in determining the outcome of the stolen identity risk check.

    Contains the following fields:

    `score` - A score from 0 to 100 indicating the likelihood that the user is a stolen identity.
    """
    synthetic_identity: Optional[RiskCheckSyntheticIdentity] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('synthetic_identity') }})
    r"""Field containing the data used in determining the outcome of the synthetic identity risk check.

    Contains the following fields:

    `score` - A score from 0 to 100 indicating the likelihood that the user is a synthetic identity.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

