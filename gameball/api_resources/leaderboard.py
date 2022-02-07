from gameball.api_requestor import APIRequestor
import gameball.utils, gameball.constants 
from datetime import datetime

def leaderboard(limit= 20, from_date=None, to_date=None, player_unique_id=None, challenge_id=None):

    api_requestor_instance = APIRequestor()

    parameters={}

    if player_unique_id is not None:
        parameters['playerUniqueId'] = player_unique_id
    
    if limit is not None:
        parameters['limit'] = limit

    if challenge_id is not None:
        parameters['challengeId'] = challenge_id

    if from_date is not None:
        parameters['from'] = from_date

    if to_date is not None:
        parameters['to'] = to_date

    # urlencode
    query= "?"
    for key in parameters:
        query+=key + "=" + str(parameters[key]) + "&"

    if len(query) == 1:
        query = ""

    # query= "?" + parse.urlparse(parameters)

    response = api_requestor_instance.request(method='GET',url=gameball.constants.leaderboard + query, params = None)
    return response