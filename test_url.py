import unittest
import requests

class UrlShortenerTests(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'
    url_to_shorten = 'http://www.example.com/thisisalongexample'
    short_url = 'cb21edc2'

    def test_encode_url(self):
        response = requests.post(f'{self.base_url}/encode', json={'url': self.url_to_shorten})
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('short_url', data)

    def test_decode_url(self):
        setup = requests.post(f'{self.base_url}/encode', json={'url': self.url_to_shorten})
        response = requests.get(f'{self.base_url}/decode/{self.short_url}')
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('original_url', data)
        self.assertEqual(data["original_url"], self.url_to_shorten)

    def test_encode_missing_url_param(self):
        response = requests.post(f'{self.base_url}/encode', json={})
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Missing "url" parameter')

    def test_decode_nonexistent_url(self):
        response = requests.get(f'{self.base_url}/decode/nonexistent')
        data = response.json()

        self.assertEqual(response.status_code, 404)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Shortened URL not found')

if __name__ == '__main__':
    unittest.main()
