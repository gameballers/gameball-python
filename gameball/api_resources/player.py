from gameball.api_requestor import APIRequestor
import gameball.constants
import gameball.utils
from gameball.models.player_object import playerObject

def initialize_player(player):
    api_requestor_instance = APIRequestor()

    body={
    "playerUniqueId": player.player_unique_id,
    "playerAttributes": player.player_attributes
    }

    response = api_requestor_instance.request(method='POST',url=gameball.constants.create_player, params = body)
    return response


def get_player_info(player_unique_id, language= None):
    api_requestor_instance = APIRequestor()

    body_hashed = gameball.utils.hash_body(player_unique_id)

    body={
    "playerUniqueId": player_unique_id,
    "hash": body_hashed
    }

    supplied_headers={}

    if language is not None:
        supplied_headers['lang'] = gameball.constants.Languages[language.name].value

    response = api_requestor_instance.request(method='POST',url=gameball.constants.player_info, params = body, headers= supplied_headers)
    return response

