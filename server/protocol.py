METHOD_LIST = 'list'
METHOD_GET = 'get'


def read_headers(raw_headers):
    """ Unserialize request headers
     :type raw_headers: string
     :return: dict
    """

    data = {}
    headers = raw_headers.split('\n')
    for pair in headers:
        pair_data = pair.split(':')
        # skip invalid headers
        if 2 is not len(pair_data):
            continue
        data[pair_data[0].strip().lower()] = pair_data[1].strip().lower()

    return data