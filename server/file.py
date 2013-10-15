from echo import EchoServer
import utils


class FileServer(EchoServer):
    def __init__(self, host, port, file):
        super(FileServer, self).__init__(host, port)
        self.file = file

    def listen(self):
        """ Starts server
        """
        self.sock.listen(1)
        while True:
            client, addr = self.sock.accept()
            self._connected(client, addr)
            self._disconnected(client, addr)
            client.close()

    def _connected(self, client, addr):
        """ In our server implementation we no need to check incoming data
        """
        self.logger.debug('Start sending file to client: %s', addr)
        for chunk in utils.read_file_by_chunks(self.file, 1024):
            self._send(chunk, client, addr)

    def _disconnected(self, client, addr):
        """ Override logging message
        """
        self.logger.debug('File transition done for client: %s', addr)