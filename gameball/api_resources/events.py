from gameball.api_requestor import APIRequestor
import gameball.constants
import gameball.utils
from gameball.models.event_object import eventObject

def send_event(event):
    api_requestor_instance = APIRequestor()

    body={
    "playerUniqueId": event.player_unique_id,
    "events": event.events
    }

    body = gameball.utils.handle_channel_merging(body, event.email, event.mobile)

    response = api_requestor_instance.request(method='POST',url=gameball.constants.events, params = body)
    return response
