"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import documentaryverification as shared_documentaryverification
from ..shared import identityverificationstatus as shared_identityverificationstatus
from ..shared import identityverificationstepsummary as shared_identityverificationstepsummary
from ..shared import identityverificationtemplatereference as shared_identityverificationtemplatereference
from ..shared import identityverificationuserdata as shared_identityverificationuserdata
from ..shared import kyccheckdetails as shared_kyccheckdetails
from ..shared import riskcheckdetails as shared_riskcheckdetails
from ..shared import selfiecheck as shared_selfiecheck
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IdentityVerificationGetResponse:
    r"""A identity verification attempt represents a customer's attempt to verify their identity, reflecting the required steps for completing the session, the results for each step, and information collected in the process."""
    client_user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_user_id') }})
    r"""A unique ID that identifies the end user in your system. This ID can also be used to associate user-specific data from other Plaid products. Financial Account Matching requires this field and the `/link/token/create` `client_user_id` to be consistent. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`."""
    completed_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completed_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp."""
    documentary_verification: Optional[shared_documentaryverification.DocumentaryVerification] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documentary_verification') }})
    r"""Data, images, analysis, and results from the `documentary_verification` step. This field will be `null` unless `steps.documentary_verification` has reached a terminal state of either `success` or `failed`."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""ID of the associated Identity Verification attempt."""
    kyc_check: Optional[shared_kyccheckdetails.KYCCheckDetails] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kyc_check') }})
    r"""Additional information for the `kyc_check` step. This field will be `null` unless `steps.kyc_check` has reached a terminal state of either `success` or `failed`."""
    previous_attempt_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous_attempt_id') }})
    r"""The ID for the Identity Verification preceding this session. This field will only be filled if the current Identity Verification is a retry of a previous attempt."""
    redacted_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redacted_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    risk_check: Optional[shared_riskcheckdetails.RiskCheckDetails] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_check') }})
    r"""Additional information for the `risk_check` step."""
    selfie_check: Optional[shared_selfiecheck.SelfieCheck] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selfie_check') }})
    r"""Additional information for the `selfie_check` step. This field will be `null` unless `steps.selfie_check` has reached a terminal state of either `success` or `failed`."""
    shareable_url: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shareable_url') }})
    r"""A shareable URL that can be sent directly to the user to complete verification"""
    status: shared_identityverificationstatus.IdentityVerificationStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of this Identity Verification attempt.


    `active` - The Identity Verification attempt is incomplete. The user may have completed part of the session, but has neither failed or passed.

    `success` - The Identity Verification attempt has completed, passing all steps defined to the associated Identity Verification template

    `failed` - The user failed one or more steps in the session and was told to contact support.

    `expired` - The Identity Verification attempt was active for a long period of time without being completed and was automatically marked as expired. Note that sessions currently do not expire. Automatic expiration is expected to be enabled in the future.

    `canceled` - The Identity Verification attempt was canceled, either via the dashboard by a user, or via API. The user may have completed part of the session, but has neither failed or passed.

    `pending_review` - The Identity Verification attempt template was configured to perform a screening that had one or more hits needing review.
    """
    steps: shared_identityverificationstepsummary.IdentityVerificationStepSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('steps') }})
    r"""Each step will be one of the following values:


    `active` - This step is the user's current step. They are either in the process of completing this step, or they recently closed their Identity Verification attempt while in the middle of this step. Only one step will be marked as `active` at any given point.

    `success` - The Identity Verification attempt has completed this step.

    `failed` - The user failed this step. This can either call the user to fail the session as a whole, or cause them to fallback to another step depending on how the Identity Verification template is configured. A failed step does not imply a failed session.

    `waiting_for_prerequisite` - The user needs to complete another step first, before they progress to this step. This step may never run, depending on if the user fails an earlier step or if the step is only run as a fallback.

    `not_applicable` - This step will not be run for this session.

    `skipped` - The retry instructions that created this Identity Verification attempt specified that this step should be skipped.

    `expired` - This step had not yet been completed when the Identity Verification attempt as a whole expired.

    `canceled` - The Identity Verification attempt was canceled before the user completed this step.

    `pending_review` - The Identity Verification attempt template was configured to perform a screening that had one or more hits needing review.

    `manually_approved` - The step was manually overridden to pass by a team member in the dashboard.

    `manually_rejected` - The step was manually overridden to fail by a team member in the dashboard.
    """
    template: shared_identityverificationtemplatereference.IdentityVerificationTemplateReference = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('template') }})
    r"""The resource ID and version number of the template configuring the behavior of a given identity verification."""
    user: shared_identityverificationuserdata.IdentityVerificationUserData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""The identity data that was either collected from the user or provided via API in order to perform an identity verification."""
    watchlist_screening_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('watchlist_screening_id') }})
    r"""ID of the associated screening."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

