import logging

class EchoWorker:
    def __init__ (self):
        self.logger = logging.getLogger('tcp-echo-worker');
    
    def handle (self, clientSock, addr):
        self.logger.debug('Client connected: %s', addr)
        clientSock.send('Type `close` to close connection')
        while True:
            data = clientSock.recv(1024)
            if data is None: break
            if 'close' == data.rstrip(): break
            clientSock.send(data)

        clientSock.close()
        self.logger.debug('Client disconnected: %s', addr)
