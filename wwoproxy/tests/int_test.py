import os
import wwoproxy.boundary.wwo as wwo
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        wwo.app.config['TESTING'] = True
        self.app = wwo.app.test_client()

    def test_hw(self):
        rv = self.app.get('/weather/12/13')
        self.assertIsNotNone(rv.data)       


if __name__ == '__main__':
    unittest.main()


