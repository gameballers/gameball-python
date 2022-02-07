import gameball.constants
from gameball.api_requestor import APIRequestor
from gameball.models.batch_object import batchObject
from gameball.exceptions.gameball_exception import GameballException, AuthenticationError, APIError

def start_batch(batch):
    api_requestor_instance = APIRequestor()

    body={
        "method": batch.method,
        "operation":batch.operation,
        "params": batch.params,
        "body": batch.body
    }

    if batch.method.upper() not in ["GET", "POST", "DELETE"]:
         raise GameballException(
                "Unrecognized HTTP method %r.  This may indicate a bug in the "
                "Gameball bindings.  Please contact support@gameball.co for "
                "assistance." % (body.method)
            )
    
    if batch.operation.lower() not in ["cashback", "redeem", "balance"]:
         raise GameballException(
                "Unrecognized operation %r.  This may indicate a bug in the "
                "Gameball bindings.  Please contact support@gameball.co for "
                "assistance." % (body.operation)
            )

    response = api_requestor_instance.request(method='POST',url=gameball.constants.start_batch, params = body)
    return response


def get_batch(batch_id):
    api_requestor_instance = APIRequestor()

    if batch_id is None:
        raise GameballException(
            "No batch id was defined"
        )

    response = api_requestor_instance.request(method='GET',url=gameball.constants.get_batch.format(batch_id= batch_id), params = None)
    return response


def delete_batch(batch_id):
    api_requestor_instance = APIRequestor()

    if batch_id is None:
        raise GameballException(
            "No batch id was defined"
        )

    response = api_requestor_instance.request(method='DELETE',url=gameball.constants.delete_batch.format(batch_id= batch_id), params = None)
    return response