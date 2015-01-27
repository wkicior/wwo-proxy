FROM fedora
MAINTAINER https://github.com/wkicior
RUN yum update -y
RUN yum install -y python-pip wget
ADD requirements .
RUN pip install -r requirements
RUN mkdir /wwo-proxy
ADD wwoproxy /wwo-proxy/wwoproxy
ADD server.py /wwo-proxy/server.py
ADD settings.py.prod /wwo-proxy/wwoproxy/settings.py
EXPOSE 80
WORKDIR /wwo-proxy

CMD python server.py

