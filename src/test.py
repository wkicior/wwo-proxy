import os
import wwo
import unittest
import tempfile
import mox
import json

from service import WwoService
from gateway import WwoGateway

class TestWwoService(unittest.TestCase):
    def setUp(self):
        self.wwo_gateway_mocker = mox.Mox()
        self.wwo_gateway = self.wwo_gateway_mocker.CreateMock(WwoGateway)
        self.wwo_service  = WwoService()
        self.wwo_service.wwo_gateway = self.wwo_gateway

    def test_get_forecast(self):
        self.wwo_gateway.init(self.wwo_service.endpoint, self.wwo_service.key)
        json_resp = json.dumps([])
        ret_resp = self.wwo_gateway.get_forecast(10, 10, self.wwo_service.days).AndReturn(json_resp)
        self.wwo_gateway_mocker.ReplayAll()
        self.wwo_service.get_forecast(10, 10)
        self.wwo_gateway_mocker.VerifyAll()
        self.assertEquals(json_resp, ret_resp)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        wwo.app.config['TESTING'] = True
        self.app = wwo.app.test_client()

    def test_hw(self):
        rv = self.app.get('/weather/12/13')
        print rv.data
        self.assertIsNotNone(rv.data)


if __name__ == '__main__':
    unittest.main()


