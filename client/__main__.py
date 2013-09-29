import socket
import argparse

parser = argparse.ArgumentParser(description='Simple client application')
parser.add_argument('port', metavar='PORT', type=int, help='port number')
parser.add_argument('host', nargs='?', metavar='HOST', default='localhost', 
                     help='host name (localhost by default)')
parser.add_argument('--udp', '-u', action='store_true', help='Use UDP protocol')

args = parser.parse_args()
