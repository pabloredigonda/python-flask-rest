import unittest
from tests.TestApp import testApp

class AuthTest(unittest.TestCase):

    def setUp(self):
        self.testApp = testApp
        self.testApp.clearDb()

    def test_user_can_register(self):
        response = self.testApp.createUser()

        self.assertEqual(200, response.status_code)
        self.assertEqual(str, type(response.json['accessToken']))

    def test_user_cannot_register_twice(self):
        response = self.testApp.createUser()

        response = self.testApp.createUser()

        self.assertEqual(400, response.status_code)
        self.assertEqual('INPUT_ERROR', response.json['error'])

    def test_user_can_login(self):
        self.testApp.createUser()

        response = self.testApp.loginUser()

        self.assertEqual(200, response.status_code)
        self.assertEqual(str, type(response.json['accessToken']))

    def test_user_cannot_login_with_invalid_credentials(self):
        response = self.testApp.loginUser()

        self.assertEqual(400, response.status_code)
        self.assertEqual('INVALID_CREDENTIALS_ERROR', response.json['error'])