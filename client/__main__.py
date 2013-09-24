import argparse

parser = argparse.ArgumentParser(description='Simple TCP/UDP Client')
parser.add_argument('port', metavar='PORT', type=int, help='Port number')
parser.add_argument('host', metavar='HOST', help='Host to listen')
parser.add_argument('-u', '--udp', action='store_true', help='Use UDP protocol, TCP used by default')

args = parser.parse_args()

