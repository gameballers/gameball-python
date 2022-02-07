from gameball.api_requestor import APIRequestor
import gameball.utils, gameball.constants 

def get_configurations(lang=None):

    api_requestor_instance = APIRequestor()

    query=""

    if lang is not None:
        query+="?lang=" + lang

    response = api_requestor_instance.request(method='GET',url=gameball.constants.config + query, params = None)

    return response