FROM fedora
MAINTAINER https://github.com/wkicior
RUN yum install -y python-pip wget
ADD requirements .
RUN pip install -r requirements
ADD src/* /src/
EXPOSE 80
WORKDIR /src

CMD python server.py

