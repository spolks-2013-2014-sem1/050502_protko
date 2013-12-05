import os


class Response(object):
    """
    Simple response object
    :type data: string
    """
    def __init__(self, data):
        self._data = data
        self._current_position = 0
        self._len = len(data)

    def get_data(self, chunk_size):
        if len(self._data) < chunk_size:
            return self._data
        # get part of a string
        cut_from = self._current_position
        self._current_position = min(self._current_position + chunk_size, self.len)

        return self._data[cut_from, self._current_position]

    def is_done(self):
        return self._current_position == self.len


class StreamResponse(Response):
    """
    Streamed response object
    use it for file streaming
    :type file_handler: file
    """
    def __init__(self, file_handler):
        super(StreamResponse, self).__init__('')
        self._file = file_handler

    def get_data(self, chunk_size):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        while True:
            data = self._file.read(chunk_size)
            if not data:
                break
            yield data

    def is_done(self):
        return self._file.tell() == os.fstat(self._file.fileno()).st_size