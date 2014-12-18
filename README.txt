# wwo-proxy microservice for fetching the weather conditions from http://www.worldweatheronline.com/api/
# You must copy the settings.py.sample into settings.py.prod and fill with our WWO key
$ cp settings.py.sample settings.py.prod; vim settings.py.prod

#BUILD:
$ docker build -t wkicior/wwo-proxy .

#RUN:
$ docker run -d -p 8000:80 wkicior/wwo-proxy


#To DEV and TEST plase copy and edit the settings file first:
$ cp settings.py.sample wwoproxy/settings.py
#DEV
$ ./dev.sh

#TEST
$ ./test.sh



