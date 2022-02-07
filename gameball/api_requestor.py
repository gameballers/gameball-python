from __future__ import absolute_import, division, print_function

import gameball.constants, gameball.http_client
from gameball.exceptions.gameball_exception import GameballException, AuthenticationError, APIError
from gameball.gameball_response import gameballResponse

import gameball


class APIRequestor(object):
    def __init__(
        self,
        key=None,
        transaction_key=None,
        client=None,
        api_base=None,
    ):
        self.api_base = api_base or gameball.constants.api_base
        self.api_key = key or gameball.api_key
        self.transaction_key = transaction_key or gameball.transaction_key

        if client:
            self._client = client
        elif gameball.default_http_client:
            self._client = gameball.default_http_client
        else:
            # If the gameball.default_http_client has not been set by the user
            # yet, we'll set it here. This way, we aren't creating a new
            # HttpClient for every request.
            gameball.default_http_client = gameball.http_client.new_default_http_client()
            self._client = gameball.default_http_client


    def request(self, method, url, params=None, headers=None):

        rcode, rbody, rheaders = self.request_raw(
            method.lower(), url, params, headers
        )
        resp = self.interpret_response(rbody, rcode, rheaders)

        return resp


    def request_raw(self, method, url, params=None, supplied_headers=None):
        """
        Mechanism for issuing an API call
        """

        if self.api_key:
            my_api_key = self.api_key
        else:
            from gameball import api_key
            my_api_key = api_key
        
        if self.transaction_key:
            my_transaction_key = self.transaction_key
        else:
            from gameball import transaction_key
            my_api_key = transaction_key

        if my_api_key is None:
            raise AuthenticationError(
                "No API key provided. (HINT: set your API key using "
                '"gameball.api_key = <API-KEY>"). You can generate API keys '
                "from the Gameball web interface.  See "
                "https://help.gameball.co/en/articles/3467114-get-your-account-integration-details-api-key-and-transaction-key "
                "for details, or email support@gameball.co if you have any "
                "questions."
            )

        if my_transaction_key is None:
            raise AuthenticationError(
                "No Secret key provided. (HINT: set your API key using "
                '"gameball.api_key = <API-KEY>"). You can generate API keys '
                "from the Gameball web interface.  See "
                "https://help.gameball.co/en/articles/3467114-get-your-account-integration-details-api-key-and-transaction-key "
                "for details, or email support@gameball.co if you have any "
                "questions."
            )

        abs_url = "%s%s" % (self.api_base, url)

        if method == "get":
            post_data = None
        elif method == "post":
            post_data = params
        elif method == "put":
            post_data = params
        elif method == "delete":
            post_data = params
        else:
            raise GameballException(
                "Unrecognized HTTP method %r.  This may indicate a bug in the "
                "Gameball bindings.  Please contact support@gameball.co for "
                "assistance." % (method)
            )

        if supplied_headers is None:
            supplied_headers={}
            
        supplied_headers['APIKey']=my_api_key
        supplied_headers['secretKey']=my_transaction_key

        rcode, rbody, rheaders = self._client.request(
            method, abs_url, supplied_headers, post_data
        )

        return rcode, rbody, rheaders

    # Mechanism of returning an object in case of 200 or exception otherwise
    def interpret_response(self, rbody, rcode, rheaders):
        try:
            resp_object = gameballResponse(rbody, rcode, rheaders)
            resp = resp_object.get_data()
        except Exception:
            # Done for boolean returns in general and for vaildate coupon specially
            if rcode == 200:
                return True
            else:
                raise GameballException(
                    "Invalid response body from API: %s "
                    "(HTTP response code was %d)" % (rbody, rcode),
                    rbody,
                    rcode,
                    rheaders,
                )
        if rcode != 200:
            resp = self.handle_error_response(rbody, rcode, resp_object.data, rheaders)

        return resp 

    # Mechanism of sending GameballException in case of non-200 responses
    def handle_error_response(self, rbody, rcode, resp, rheaders):
        try:
            error_message = resp["message"]
            error_code = resp["code"]
            message = "%s (GameballException with error code %s)" % (error_message, error_code)
        except (KeyError, TypeError):
            raise APIError(
                "Invalid response object from API: %r (HTTP response code "
                "was %d)" % (rbody, rcode),
                rbody,
                rcode,
                resp,
            )
        return GameballException(message, rbody, rcode, resp, rheaders)


    

    