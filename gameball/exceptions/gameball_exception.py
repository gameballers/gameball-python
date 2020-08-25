from __future__ import absolute_import, division, print_function

class GameballException(Exception):
    def __init__(
        self,
        message=None,
        http_body=None,
        json_body=None,
        headers=None,
        code=None,
    ):
        super(GameballException, self).__init__(message)

        self._message = message
        self.http_body = http_body
        self.json_body = json_body
        self.headers = headers or {}
        self.code = code

    def __str__(self):
        msg = self._message or "<empty message>"
        return msg

    # Returns the underlying `Exception` (base class) message, which is usually
    # the raw message returned by Gameball's API. This was previously available
    # in python2 via `error.message`. Unlike `str(error)`, it omits "Request
    # req_..." from the beginning of the string.
    @property
    def user_message(self):
        return self._message

    def __repr__(self):
        return "%s(message=%r)" % (
            self.__class__.__name__,
            self._message,
        )


class AuthenticationError(GameballException):
    pass

class APIError(GameballException):
    pass

