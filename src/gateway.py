import json
import urllib
import urllib2

#from settings import WWO_TIMEOUT

class WwoGateway:
    def init(self, endpoint, key):
        self.endpoint = endpoint
        self.key = key
        #self.timeout = WWO_TIMEOUT

    def get_forecast(self, latitude, longitude, days):
        values = {'q' : latitude + "," + longitude,
                  'format' : 'json',
                  'key' : self.key,
                  'num_of_days' : days,}

        data = urllib.urlencode(values)
        req = urllib2.Request(self.endpoint, data)
        response = urllib2.urlopen(self.endpoint + "?" + data)
        the_page = response.read()
        return the_page
     
        
