from gameball.api_requestor import APIRequestor
import gameball.constants
from gameball.models.event_object import eventObject

def send_event(event):
    api_requestor_instance = APIRequestor()

    body={
    "playerUniqueId": event.player_unique_id,
    "events": event.events
    }

    if event.player_attributes is not {}:
        body["playerAttributes"] = event.player_attributes

    response = api_requestor_instance.request(method='POST',url=gameball.constants.events, params = body)
    return response
