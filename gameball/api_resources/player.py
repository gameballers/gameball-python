from gameball.api_requestor import APIRequestor
import gameball.constants
import gameball.utils
from gameball.models.player_object import playerObject, playerAttributes

def initialize_player(player):
    api_requestor_instance = APIRequestor()
    player_attributes = player.player_attributes.__dict__

    body={
        "playerUniqueId": player.player_unique_id,
        "playerAttributes": player_attributes,
        "referrerCode": player.referrer_code,
        "levelOrder": player.level_order
    }

    body = gameball.utils.handle_channel_merging(body, player.email, player.mobile)

    response = api_requestor_instance.request(method='POST', url=gameball.constants.create_player, params = body)
    return response

def get_player_balance(player_unique_id, email = None, mobile = None):

    api_requestor_instance = APIRequestor()
    
    to_replace = email or mobile or player_unique_id

    response = api_requestor_instance.request(method='GET', url=gameball.constants.player_balance.format(player_unique_id = to_replace), params = None)
    return response

def get_player_progress(player_unique_id, email = None, mobile = None):

    api_requestor_instance = APIRequestor()

    to_replace = email or mobile or player_unique_id

    response = api_requestor_instance.request(method='GET', url=gameball.constants.player_progress.format(player_unique_id = to_replace), params = None)
    return response


def get_player_info(player_unique_id, email = None, mobile = None, language= None):
    api_requestor_instance = APIRequestor()

    supplied_headers={}

    if language is not None:
        supplied_headers['lang'] = gameball.constants.Languages[language.name].value

    to_replace = email or mobile or player_unique_id

    response = api_requestor_instance.request(method='GET',url=gameball.constants.player_info.format(player_unique_id = to_replace), params = None, headers= supplied_headers)
    return response

def attach_tags(player_unique_id, tags, email = None, mobile = None):
    api_requestor_instance = APIRequestor()

    body={
        "tags": tags
    }

    to_replace = email or mobile or player_unique_id

    response = api_requestor_instance.request(method='POST',url=gameball.constants.player_tags.format(player_unique_id = to_replace), params = body, headers= None)
    return response

def detach_tags(player_unique_id, tags, email = None, mobile = None):
    api_requestor_instance = APIRequestor()

    body={
        "tags": tags
    }

    to_replace = email or mobile or player_unique_id

    response = api_requestor_instance.request(method='DELETE',url=gameball.constants.player_tags.format(player_unique_id = to_replace), params = body, headers= None)
    return response

def get_notifications(player_unique_id, is_read=None, lang=None, page=None, limit=None, email = None, mobile = None):
    api_requestor_instance = APIRequestor()

    parameters={}
    
    if limit is not None:
        parameters['limit'] = limit

    if is_read is not None:
        parameters['isRead'] = is_read

    if lang is not None:
        parameters['lang'] = lang

    if page is not None:
        parameters['page'] = page

    # urlencode
    query= "?"
    for key in parameters:
        query+=key + "=" + str(parameters[key]) + "&"
    
    if len(query) == 1:
        query = ""

    to_replace = email or mobile or player_unique_id

    response = api_requestor_instance.request(method='GET',url=gameball.constants.player_notifications.format(player_unique_id = to_replace) + query, params = None, headers= None)
    return response

