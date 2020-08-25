from gameball.api_requestor import APIRequestor
import gameball.utils, gameball.constants 
from datetime import datetime
from gameball.models.reward_object import rewardObject

def get_player_balance(player_unique_id):

    api_requestor_instance = APIRequestor()
    
    body_hashed = gameball.utils.hash_body(player_unique_id)

    body={
    "playerUniqueId": player_unique_id,
    "hash": body_hashed
    }
    response = api_requestor_instance.request(method='POST',url=gameball.constants.player_points_balance, params = body)
    return response


def hold_points(player_unique_id, amount):

    api_requestor_instance = APIRequestor()
    body_hashed = gameball.utils.hash_body(player_unique_id, datetime.utcnow().strftime("%y%m%d%H%M%S"), amount)

    body={
    "playerUniqueId": player_unique_id,
    "amount":amount,
    "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
    "hash": body_hashed
    }
    response = api_requestor_instance.request(method='POST',url=gameball.constants.hold_Points, params = body)
    return response


def redeem_points(player_unique_id, hold_reference, transaction_id):

    api_requestor_instance = APIRequestor()
    body_hashed = gameball.utils.hash_body(player_unique_id, datetime.utcnow().strftime("%y%m%d%H%M%S"))

    body={
    "playerUniqueId": player_unique_id,
    "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
    "hash": body_hashed,
    "holdReference":hold_reference,
    "transactionId":transaction_id
    }

    response = api_requestor_instance.request(method='POST',url=gameball.constants.redeem_points, params = body)
    return response


def reverse_transaction(player_unique_id, transaction_id, reversed_transaction_id):

    api_requestor_instance = APIRequestor()
    body_hashed = gameball.utils.hash_body(player_unique_id, datetime.utcnow().strftime("%y%m%d%H%M%S"))

    body={
    "playerUniqueId": player_unique_id,
    "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
    "hash": body_hashed,
    "transactionId":transaction_id,
    "reversedTransactionId":reversed_transaction_id 
    }

    response = api_requestor_instance.request(method='POST',url=gameball.constants.reverse_transaction, params = body)
    return response


def reverse_hold(player_unique_id, hold_reference):

    api_requestor_instance = APIRequestor()
    body_hashed = gameball.utils.hash_body(player_unique_id, datetime.utcnow().strftime("%y%m%d%H%M%S"))

    body={
    "playerUniqueId": player_unique_id,
    "holdReference":hold_reference,
    "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
    "hash": body_hashed
    }
    response = api_requestor_instance.request(method='POST',url=gameball.constants.hold_Points, params = body)
    return response


def reward_points(reward):

    api_requestor_instance = APIRequestor()
    body_hashed = gameball.utils.hash_body(reward.player_unique_id, datetime.utcnow().strftime("%y%m%d%H%M%S"), reward.amount)

    body={
    "playerUniqueId": reward.player_unique_id,
    "amount":reward.amount,
    "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
    "hash": body_hashed,
    "transactionId":reward.transaction_id
    }

    if reward.player_attributes != {}:
        body["playerAttributes"] = reward.player_attributes

    response = api_requestor_instance.request(method='POST',url=gameball.constants.reward_points, params = body)
    return response
    