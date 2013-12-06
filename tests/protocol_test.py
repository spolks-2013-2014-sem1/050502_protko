import unittest
from server import protocol


class ProtocolTest(unittest.TestCase):

    def test_read_headers_list(self):
        raw_data = 'Method: LIST\nPath: /'
        data = protocol.read_headers(raw_data)
        self.assertDictEqual({
            'method': 'list',
            'path': '/'
        }, data, 'Should parse LIST requests with path')

    def test_read_invalid_headers(self):
        raw_data = 'Method: LIST\nPath\nTest : value'
        data = protocol.read_headers(raw_data)
        self.assertDictEqual({
            'method': 'list',
            'test': 'value'
        }, data, 'Should skip all invalid pairs')


def main():
    unittest.main()

if __name__ == '__main__':
    main()