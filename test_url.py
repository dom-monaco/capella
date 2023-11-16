import unittest
import requests

class UrlShortenerTests(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'

    def test_encode_url(self):
        url_to_shorten = 'http://www.example.com/thisisalongexample'
        response = requests.post(f'{self.base_url}/encode', json={'url': url_to_shorten})
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('short_url', data)

    def test_decode_url(self):
        return True

    def test_encode_missing_url_param(self):
        return True

    def test_decode_nonexistent_url(self):
        return True

if __name__ == '__main__':
    unittest.main()
