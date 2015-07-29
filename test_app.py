# coding: utf-8

from app import app
import unittest


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.index = self.client.get('/')
        self.invite = self.client.post(
            '/invite',
            data=dict(email=u'guilherme-louro@hotmail.com'),
            follow_redirects=True
        )

    def test_get_index(self):
        self.assertEqual(self.index.status_code, 200)

    def test_post_invite(self):
        self.assertEqual(self.invite.status_code, 200)

    def test_get_invite(self):
        self.invite = self.client.get('/invite')
        self.assertEqual(self.invite.status_code, 302)


if __name__ == '__main__':
    unittest.main()
