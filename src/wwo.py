from flask import Flask, request
from service import WwoService
import json

app = Flask(__name__)

@app.route("/weather/<latitude>/<longitude>")
def weather(latitude, longitude):
    wwo_service = WwoService()
    forecast_dic =  wwo_service.get_forecast(latitude, longitude)
    return json.dumps(forecast_dic)

if __name__ == "__main__":
    app.run()

