# wwo-proxy microservice for fetching the weather conditions from http://www.worldweatheronline.com/api/
# You must copy the settings.py.sample into settings.py.prod and fill with our WWO key
$ cp settings.py.sample settings.py.prod; vim settings.py.prod

#BUILD:
$ docker build -t wkicior/wwo-proxy .

#RUN:
$ docker run -d --name wwo-proxy -p 8000:80 wkicior/wwo-proxy


#To DEV and TEST plase copy and edit the settings file first:
$ cp settings.py.sample wwoproxy/settings.py
#DEV
$ ./dev.sh

#TEST
$ ./test.sh

#BDD TEST
$ behave wwoproxy/tests/integration/

#Use
$ wget http://wwo-proxy/forecast/12/13
#or
$ wget http://localhost:8000/forecast/12/13

