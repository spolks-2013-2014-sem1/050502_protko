import socket

class Tcp:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def bind(self):
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSock.bind((self.host, self.port))
        
        return True
    
    def listen(self):
        self.serverSock.listen(1)
        while True:
            clientSock, addr = self.serverSock.accept()
            self.handle(clientSock, addr)

    def handle(self, clientSock, addr):
        self.worker.handle(clientSock, addr)

    def registerWorker(self, worker):
        self.worker = worker

    def shutdown(self):
        self.serverSock.close()
