from EchoWorker import EchoWorker

# from stackoverflow
def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

class FileWorker(EchoWorker):
    def __init__(self, file):
        self.file = file
        # initialize logger
        EchoWorker.__init__(self)

    def handle(self, clientSock, addr):
        self.logger.debug('Client connected: %s', addr)
        for piece in read_in_chunks(self.file):
            clientSock.send(piece)
        clientSock.close()
        self.logger.debug('Done, disconnect client: %s', addr)
