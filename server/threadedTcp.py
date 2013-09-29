import threading
from tcp import Tcp

class ThreadedTcp(Tcp):
    def __init__(self, host, port):
        Tcp.__init__(self, host, port)
    
    def handle(self, clientSock, addr):
        handler = threading.Thread(target=self.worker.handle, args=[clientSock, addr])
        handler.start()
        print 'Thread started!'
