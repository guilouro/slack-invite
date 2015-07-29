# coding: utf-8

from app import app
import unittest


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.index = self.client.get('/')
        self.invite = self.client.get('/invite')

    def test_get_index(self):
        self.assertEqual(self.index.status_code, 200)

    def test_get_invite(self):
        self.assertEqual(self.invite.status_code, 200)

    def test_content_type(self):
        self.assertEqual(self.invite.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
