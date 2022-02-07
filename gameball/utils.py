import hashlib
from gameball.exceptions.gameball_exception import GameballException, AuthenticationError
import gameball
from datetime import datetime, timezone
# import pytz


# Mechanism of hashing the body to include transaction key in case of transaction requests
def hash_body(player_unique_id = '', transaction_time = '', amount = ''):

    if gameball.transaction_key is None:
            raise AuthenticationError(
                "No Transaction key provided. (HINT: set your Transaction key using "
                '"gameball.transaction_key = <Transaction-KEY>"). You can generate Trransaction keys '
                "from the Gameball web interface.  See "
                "https://help.gameball.co/en/articles/3467114-get-your-account-integration-details-api-key-and-transaction-key "
                "for details, or email support@gameball.co if you have any "
                "questions."
            )

    body = str(player_unique_id)+":"+transaction_time+":"+str(amount)+":"+gameball.transaction_key
    hashed = hashlib.sha1(body.encode())
    return hashed.hexdigest()


# Mechanism of encoding date in the way Gameball APIs accepts it
def encode_date(date_time):
    # pytz instead of timezone
    date_time_utc = date_time.replace(tzinfo=timezone.utc)
    date_time_iso = date_time_utc.isoformat()
    return(str(date_time_iso).replace('+00:00', 'Z'))


def handle_channel_merging(obj, email, mobile):
    if (email != None):
        obj.email = email
    
    if (mobile != None):
        obj.mobile = mobile
        
    return obj