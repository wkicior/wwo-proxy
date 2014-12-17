import os
import wwo
import unittest
import tempfile
import mox
import json

from service import WwoService
from gateway import WwoGateway
from parser import Parser

class TestWwoService(unittest.TestCase):
    def setUp(self):
        self.wwo_gateway_mocker = mox.Mox()
        self.wwo_gateway = self.wwo_gateway_mocker.CreateMock(WwoGateway)
        self.parser_mocker = mox.Mox()
        self.parser = self.parser_mocker.CreateMock(Parser)

        self.wwo_service  = WwoService()
        self.wwo_service.wwo_gateway = self.wwo_gateway
        self.wwo_service.parser = self.parser

    def test_get_forecast(self):
        self.wwo_gateway.init(self.wwo_service.endpoint, self.wwo_service.key)
        json_resp = json.dumps([0])
        parsed_resp = json.dumps([1])
        self.wwo_gateway.get_forecast(10, 10, self.wwo_service.days).AndReturn(json_resp)
        self.parser.parse(json_resp).AndReturn(parsed_resp)
        self.wwo_gateway_mocker.ReplayAll()
        self.parser_mocker.ReplayAll()

        ret_resp = self.wwo_service.get_forecast(10, 10)
        self.wwo_gateway_mocker.VerifyAll()
        self.parser_mocker.VerifyAll()
        self.assertEquals(parsed_resp, ret_resp)

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        with open('../res/sample_wwo_output.json', 'r') as json_file:            
            self.input = json_file.read()
        with open('../res/sample_wwo_proxy_output.json', 'r') as json_file:            
            self.output = json.load(json_file)

    def test_parse(self):
        res = self.parser.parse(self.input)
        self.maxDiff = None
        self.assertEquals(self.output, res)

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


