import argparse
import signal
import sys
import server
import logging

parser = argparse.ArgumentParser(description='Simple Echo TCP Server')
parser.add_argument('port', type=int, help='Port to listen')
parser.add_argument('host', nargs='?', default='localhost', help='Hostname to listen (default: localhost)')
parser.add_argument('--verbose', '-v', action='store_true', help='Display debug information')
parser.add_argument('--file', '-f', metavar='PATH', required=True, type=argparse.FileType('r'),
                    help='path to file which will be transferred to clients')

args = parser.parse_args()

# allow to show debug messages in verbose mode
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)


def exit_gracefully(signal, frame):
    print '\nBye'
    if s is not None:
        s.shutdown()
    args.file.close()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_gracefully)

s = server.FileServer(args.host, args.port, args.file)
s.bind()
s.listen()