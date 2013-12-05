import sys
from common import create_argument_parser

parser = create_argument_parser('Simple server implementation, which uses TCP/UDP as transport')
options = parser.parse_args()

# check for supported features
error = None
if not error and options.udp:
    error = 'Sorry, this version does not supports UDP yet'
if not error and not options.echo:
    error = 'Sorry, this version does not support file sharing yet'
if error:
    print error, "\n"
    sys.exit(1)

