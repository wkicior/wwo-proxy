# wwo-proxy microservice for fetching the weather conditions from http://www.worldweatheronline.com/api/

#BUILD:
docker build -t wkicior/wwo-proxy .

#RUN:
docker run -d -p 8000:80 wkicior/wwo-proxy



