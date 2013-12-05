class Request(object):
    """
    Request handler
    :type data: dict
    """
    def __init__(self, data):
        self._data = data

    def get(self, name, default):
        if self._data.has_key(name):
            return self._data[name]
        return default

    def has(self, name):
        return self._data.has_key(name)