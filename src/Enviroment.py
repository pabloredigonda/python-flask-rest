import os

class Enviroment:

    def __init__(self):
        self.jwtSecret = os.getenv('JWT_SECRET')
        self.mongoSettings = os.getenv('MONGODB_SETTINGS')
        