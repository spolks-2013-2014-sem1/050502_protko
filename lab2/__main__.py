import argparse
import signal
import sys
import server
import logging

parser = argparse.ArgumentParser(description='Simple Echo TCP Server')
parser.add_argument('port', type=int, help='Port to listen')
parser.add_argument('host', nargs='?', default='localhost', help='Hostname to listen (default: localhost)')
parser.add_argument('--verbose', '-v', action='store_true', help='Display debug information')

args = parser.parse_args()

# allow to show debug messages in verbose mode
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)


def exit_gracefully(signal, frame):
    print '\nBye'
    if s is not None:
        s.shutdown()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_gracefully)

s = server.EchoServer(args.host, args.port)
s.bind()
s.listen()