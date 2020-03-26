import unittest
from tests.TestApp import testApp

class UserTest(unittest.TestCase):

    def setUp(self):
        self.testApp = testApp
        self.testApp.clearDb()

    def test_can_get_user(self):
        #Given
        response = self.testApp.createUser()
        token = response.json['accessToken']
        
        # When
        response = self.testApp.getUser(token)

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual("Pablo", response.json['firstName'])
        self.assertEqual("Redigonda", response.json['lastName'])
        self.assertEqual("pabloredigonda@gmail.com", response.json['email'])

    def test_cannot_get_user_without_valid_token(self):
        #Given
        token = 'invalidtoken'
        
        # When
        response = self.testApp.getUser(token)

        # Then
        self.assertEqual(401, response.status_code)
        self.assertEqual("UNAUTHORIZED_ERROR", response.json['error'])