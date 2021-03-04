import unittest
import codecs
from flask import request

from app import my_app


class TestHome(unittest.TestCase):
    def setUp(self):
        app = my_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        self.assertIn('Hello', self.response.data.decode('utf-8'))

    def test_content(self):
        with codecs.open("./templates/index.html", 'r') as f:
            response_srt = self.response.data.decode('utf-8')
            self.assertIn(f.read(), response_srt)

    def test_bootstrap_css(self):
        response_srt = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_srt)

    def test_profile_image(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<img src="', response_str)
        self.assertIn('class="img-circle"', response_str)

    def test_link(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('href="http://twitter.com/cuducos"', response_str)
        self.assertIn('>Me siga no Twitter</a>', response_str)


class TestPerfis(unittest.TestCase):
    def setUp(self):
        app = my_app.test_client()
        self.response = app.get('/<perfil>')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)


if __name__ == '__main__':
    unittest.main()
