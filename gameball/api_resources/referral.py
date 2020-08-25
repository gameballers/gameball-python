from gameball.api_requestor import APIRequestor
from gameball.models.referral_object import referralObject
import gameball.constants

def create_referral(referral):
    api_requestor_instance = APIRequestor()

    body={
    "playerUniqueId": referral.player_unique_id,
    "playerCode": referral.player_code
    }

    if referral.player_attributes is not {}:
        body["playerAttributes"] = referral.player_attributes

    response = api_requestor_instance.request(method='POST',url=gameball.constants.referral, params = body)
    return response