FROM fedora
MAINTAINER https://github.com/wkicior
RUN yum install -y python-pip wget
RUN pip install Flask cherrypy
ADD src/* /src/
EXPOSE 80
WORKDIR /src

CMD python server.py

