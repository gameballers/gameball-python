from gameball.api_requestor import APIRequestor
import gameball.utils, gameball.constants 

def mark_notifications(notification_ids):

    api_requestor_instance = APIRequestor()

    body={
        "notificationIds": notification_ids
    }

    response = api_requestor_instance.request(method='PUT',url=gameball.constants.mark_notifications, params = body)

    return response