from flask import Flask, request
from service import WwoService
app = Flask(__name__)

@app.route("/weather/<latitude>/<longitude>")
def weather(latitude, longitude):
    wwo_service = WwoService()
    return wwo_service.get_forecast(latitude, longitude)

if __name__ == "__main__":
    app.run()

