import json
import urllib
import urllib2
import pybreaker

from wwoproxy.settings import WWO_TIMEOUT

wwo_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)


class WwoGateway:
    def init(self, endpoint, key):
        self.endpoint = endpoint
        self.key = key
        self.timeout = WWO_TIMEOUT
        
    @wwo_breaker
    def get_forecast(self, latitude, longitude, days):
        values = {'q' : latitude + "," + longitude,
                  'format' : 'json',
                  'key' : self.key,
                  'num_of_days' : days,}

        data = urllib.urlencode(values)
        req = urllib2.Request(self.endpoint, data)
        response = urllib2.urlopen(self.endpoint + "?" + data, timeout = self.timeout)
        the_page = response.read()
        return the_page
     
        
