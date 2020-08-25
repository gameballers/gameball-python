import gameball.constants
from gameball.api_requestor import APIRequestor
from gameball.models.action_object import actionObject

def send_action(action):
    api_requestor_instance = APIRequestor()

    body={
    "playerUniqueId": action.player_unique_id,
    "playerAttributes":action.player_attributes,
    "events": action.events
    }

    if action.points_transaction is not None:
        body["pointsTransaction"] = action.points_transaction

    response = api_requestor_instance.request(method='POST',url=gameball.constants.send_action, params = body)
    return response
