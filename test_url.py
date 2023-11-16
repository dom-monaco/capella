import unittest
import requests

class UrlShortenerTests(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'

    def test_encode_url(self):
        return True

    def test_decode_url(self):
        return True

    def test_encode_missing_url_param(self):
        return True

    def test_decode_nonexistent_url(self):
        return True

if __name__ == '__main__':
    unittest.main()
    