from behave import given, when, then
import json
import requests
import datetime
from hamcrest import assert_that, equal_to, not_none

HOST = 'http://localhost:5000'

@given("Flask app is running")
def start_app(context):
    response = requests.get(HOST)
    assert response.status_code == 200

@when("We request a forecast")
def request_forecast(context):
    response = requests.get(HOST+'/forecast/54.758611/18.509444')
    context.forecast = response.json()
    assert_that(response.status_code, equal_to(200))

@then("We get a forecast")
def verify_forecast(context):
    assert_that(context.forecast['forecast'], not_none)
