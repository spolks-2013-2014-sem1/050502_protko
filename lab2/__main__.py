import server.worker as worker
import server.tcp as server
import argparse
import signal
import sys

parser = argparse.ArgumentParser(description='Simple synchtonous TCP server')
parser.add_argument('port', metavar='PORT', type=int, help='port number')
parser.add_argument('host', nargs='?', metavar='HOST', default='localhost', 
                     help='host name (localhost by default)')

args = parser.parse_args()

def graceful_shutdown(signal, frame):
    s.shutdown()
    print '\nBye'
    sys.exit(0)

signal.signal(signal.SIGINT, graceful_shutdown)

s = server.Tcp(args.host, args.port)
if not s.bind():
    print 'Unable to create socket'
    sys.exit(1)

worker = worker.EchoWorker()
s.registerWorker(worker)
s.listen()


