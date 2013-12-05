import argparse

def create_argument_parser(description):
    """ Create instance of parser and set all common options
    :type description: str
    :return: ArgumentParser
    """
    parser = argparse.ArgumentParser(description=description)

    parser.version = '1.0'
    parser.add_argument('port', type=int, help='Port to listen')
    parser.add_argument('host', nargs='?', default='localhost', help='Hostname to listen (default: localhost)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Display debug information')
    parser.add_argument('--echo', '-e', action='store_true', help='Run echo server')
    parser.add_argument('--udp', '-u', action='store_true', help='Use UDP as transport')

    return parser