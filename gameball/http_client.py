from __future__ import absolute_import, division, print_function

import sys
import threading
import json
import gameball.exceptions.gameball_exception


try:
    import requests
except ImportError:
    requests = None
else:
    try:
        # Require version 0.8.8, but don't want to depend on distutils
        version = requests.__version__
        major, minor, patch = [int(i) for i in version.split(".")]
    except Exception:
        # Probably some new-fangled version, so it should support verify
        pass
    else:
        if (major, minor, patch) < (0, 8, 8):
            sys.stderr.write(
                "Warning: the Gameball library requires that your Python "
                '"requests" library be newer than version 0.8.8, but your '
                '"requests" library is version %s. We recommend upgrading your'
                '"requests" library. If you have any questions, please contact'
                'support@gameball.co. (HINT: running "pip install -U requests" '
                'should upgrade your requests library to the latest version.)' % (version,)
            )
            requests = None


# Mechanism of creating new client (Done only in the first request)
def new_default_http_client(*args, **kwargs):
    
    return HTTPClient(*args, **kwargs)


class HTTPClient(object):

    def __init__(self, timeout=80, session=None):
        self._session = session
        self._timeout = timeout

        self._thread_local = threading.local()


    def request(self, method, url, headers, post_data=None):

        if getattr(self._thread_local, "session", None) is None:
            self._thread_local.session = self._session or requests.Session()

        try:
            result = self._thread_local.session.request(
                method,
                url,
                headers=headers,
                json=post_data,
                timeout=self._timeout
            )
        except TypeError as e:
            raise TypeError(
                "Warning: It looks like your installed version of the "
                '"requests" library is not compatible with Gameball\'s '
                "usage thereof. (HINT: The most likely cause is that "
                'your "requests" library is out of date. You can fix '
                'that by running "pip install -U requests".) The '
                "underlying error was: %s" % (e,)
            )

        # This causes the content to actually be read, which could cause
        # e.g. a socket timeout. TODO: The other fetch methods probably
        # are susceptible to the same and should be updated.
        content = result.content
        status_code = result.status_code
       
        return status_code, content, result.headers


    def close(self):
        if getattr(self._thread_local, "session", None) is not None:
            self._thread_local.session.close()
