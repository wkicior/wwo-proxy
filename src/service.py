from gateway import WwoGateway
from parser import Parser
try:
    from settings import *
except:
    print "ERROR! Please use settings.py.sample template to create your settings.py file"

class WwoService:
    def __init__(self):
        self.wwo_gateway = WwoGateway()
        self.parser = Parser()
        self.key = WWO_KEY
        self.endpoint = WWO_ENDPOINT
        self.days = 5

    def get_forecast(self, latitude, longitude):
        self.wwo_gateway.init(self.endpoint, self.key)
        wwo_resp = self.wwo_gateway.get_forecast(latitude, longitude, self.days)
        return self.parser.parse(wwo_resp)
