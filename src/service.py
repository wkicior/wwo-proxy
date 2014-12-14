from gateway import WwoGateway
try:
    from settings import *
except:
    print "ERROR! Please use settings.py.sample template to create your settings.py file"

class WwoService:
    def __init__(self):
        self.wwo_gateway = WwoGateway()
        self.key = WWO_KEY
        self.endpoint = WWO_ENDPOINT
        self.days = 5

    def get_forecast(self, latitude, longitude):
        self.wwo_gateway.init(self.endpoint, self.key)
        return self.wwo_gateway.get_forecast(latitude, longitude, self.days)
