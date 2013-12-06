import unittest
from server import protocol


class ProtocolTest(unittest.TestCase):

    def test_read_headers_list(self):
        raw_data = 'Method: LIST\nPath: /'
        data = protocol.read_headers(raw_data)
        self.assertDictEqual({
            'method': protocol.METHOD_LIST,
            'path': '/'
        }, data, 'Should parse LIST requests with path')


def main():
    unittest.main()

if __name__ == '__main__':
    main()