from dotenv import load_dotenv
load_dotenv()

from .Enviroment import Enviroment
from .Application import Application

def create_app():
    enviroment = Enviroment()
    application = Application(enviroment)
    return application.init()