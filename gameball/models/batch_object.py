class batchObject(object):
    def __init__(
        self,
        method,
        operation,
        params = {},
        body = {}
    ):
        self.method = method
        self.operation = operation
        self.params = params
        self.body = body
