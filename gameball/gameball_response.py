import json

class gameballResponse(object):
    def __init__(self, body, code, headers):
        self.body = body
        self.code = code
        self.headers = headers
        
        if body != b'':
            self.data = json.loads(body)

    def get_data(self):
        try:
            return self.data
        except KeyError:
            return None

    def isSuccess():
      return self.code == 200
