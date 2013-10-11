import socket
import logging

class EchoServer:
    """ Simple echo server on TCP sockets
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
        self.logger = logging.getLogger('server')

    def bind(self):
        """ Creates new socket object and prepares it for listening
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        """ Starts server
        """
        self.sock.listen(1)
        while True:
            client, addr = self.sock.accept()
            self.__connected(client, addr)
            while True:
                data = client.recv(1024)
                if not data or 'close' == data.rstrip():
                    break
                self.__progress(data, client, addr)
            self.__disconnected(client, addr)
            client.close()

    def __connected(self, client, addr):
        """ Starts processing of client connection
        """
        self.logger.debug('Client connected: address %s', addr)
        client.send('\nType `close` to close connection')

    def __progress(self, chunk, client, addr):
        """ Processing of incoming data
        """
        self.logger.debug('Received data from client: %s', addr)
        self.__send(chunk, client, addr)

    def __send(self, data, client, addr):
        """ Sends data to client
        """
        self.logger.debug('Send data to client: %s', addr)
        client.send(data)

    def __disconnected(self, client, addr):
        """ Handling client disconnection
        """
        self.logger.debug('Client disconnected: %s', addr)

    def shutdown(self):
        """ Graceful shutdown of server
        """
        self.logger.debug('Shutdown server')
        if self.sock is not None:
            self.sock.close()