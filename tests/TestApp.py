from dotenv import load_dotenv
load_dotenv()
import os

import json
from src.Application import Application
from src.Enviroment import Enviroment
from mongoengine.connection import _get_db

class TestApp:

    def __init__(self):
        enviroment = Enviroment()
        application = Application(enviroment)
        self.app = application.init()
        self.client = self.app.test_client()
        self.db = self.app.di.database().get_db()


    def get(self, url: str, token: str = None):
        headers = {"Content-Type": "application/json"}

        if token:
            headers['Authorization'] = 'Bearer {}'.format(token)

        return self.client.get(url, headers=headers)

    def post(self, url: str, payload: dict):
        return self.client.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
    
    def clearDb(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)


    def createUser(self):
        payload = {
            "firstName": "Pablo",
            "lastName": "Redigonda",
            "email": "pabloredigonda@gmail.com",
            "password": "example-password"
        }

        return self.post('/auth/register', payload=payload)

    def loginUser(self):
        payload = {
            "email": "pabloredigonda@gmail.com",
            "password": "example-password"
        }

        return self.post('/auth/login', payload=payload)

    def getUser(self, token: str):
        return self.get('/user/me', token=token)

testApp = TestApp()