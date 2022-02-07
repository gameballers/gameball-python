from gameball.api_requestor import APIRequestor
import gameball.utils, gameball.constants 
from datetime import datetime
from gameball.models.reward_object import rewardObject


def hold_points(player_unique_id, amount, email = None, mobile = None):

    api_requestor_instance = APIRequestor()

    body={
        "playerUniqueId": player_unique_id,
        "amount":amount,
        "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
    }

    body = gameball.utils.handle_channel_merging(body, email, mobile)

    response = api_requestor_instance.request(method='POST',url=gameball.constants.hold_Points, params = body)
    return response


def redeem_points(player_unique_id, transaction_id, redeemed_amount= None, hold_reference= None, email = None, mobile = None):

    api_requestor_instance = APIRequestor()

    body={
        "playerUniqueId": player_unique_id,
        "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
        "holdReference":hold_reference,
        "redeemedAmount":redeemed_amount,
        "transactionId":transaction_id
    }

    body = gameball.utils.handle_channel_merging(body, email, mobile)

    response = api_requestor_instance.request(method='POST',url=gameball.constants.redeem_points, params = body)
    return response


def refund(player_unique_id, transaction_id, reversed_transaction_id, amount=None, email = None, mobile = None):

    api_requestor_instance = APIRequestor()

    body={
        "playerUniqueId":player_unique_id,
        "transactionId":transaction_id,
        "reverseTransactionId":reversed_transaction_id,
        "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
        "amount": amount
    }

    body = gameball.utils.handle_channel_merging(body, email, mobile)

    response = api_requestor_instance.request(method='POST',url=gameball.constants.refund_transaction, params = body)
    return response


def reverse_hold(hold_reference):

    api_requestor_instance = APIRequestor()

    response = api_requestor_instance.request(method='DELETE',url=gameball.constants.reverse_hold.format(hold_reference= hold_reference), params = None)
    return response


def reward_points(reward):

    api_requestor_instance = APIRequestor()

    body={
        "playerUniqueId": reward.player_unique_id,
        "amount":reward.amount,
        "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
        "transactionId":reward.transaction_id,
        "merchant": reward.merchant
    }

    body = gameball.utils.handle_channel_merging(body, reward.email, reward.mobile)

    response = api_requestor_instance.request(method='POST',url=gameball.constants.reward_points, params = body)
    return response

def manual_transaction(player_unique_id, transaction_id, username, reason, amount=None, points=None, email = None, mobile = None):

    api_requestor_instance = APIRequestor()

    body={
        "playerUniqueId":player_unique_id,
        "amount": amount,
        "points": points,
        "transactionId":transaction_id,
        "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
        "username": username,
        "reason": reason
    }

    body = gameball.utils.handle_channel_merging(body, email, mobile)

    response = api_requestor_instance.request(method='POST',url=gameball.constants.manual_transaction, params = body)
    return response

def list_transactions(page= 1, limit= 50, direction= None, from_date=None, to_date=None, transaction_id=None, status=None):

    api_requestor_instance = APIRequestor()

    parameters={}

    if page is not None:
        parameters['page'] = page
    
    if limit is not None:
        parameters['limit'] = limit

    if direction is not None:
        parameters['direction'] = direction

    if from_date is not None:
        parameters['from'] = from_date

    if to_date is not None:
        parameters['to'] = to_date

    if transaction_id is not None:
        parameters['transactionId'] = transaction_id
    
    if status is not None:
        parameters['status'] = status

    # urlencode
    query= "?"
    for key in parameters:
        query+=key + "=" + str(parameters[key]) + "&"

    # query= "?" + parse.urlparse(parameters)

    response = api_requestor_instance.request(method='GET',url=gameball.constants.list_transactions + query, params = None)
    return response
    