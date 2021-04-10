FROM python:3

RUN mkdir docker_root
RUN mkdir /root/.aws
RUN cd docker_root
WORKDIR /docker_root
RUN mkdir test

ADD /logic /docker_root/test
ADD requirements.txt /docker_root
ADD credentials /root/.aws

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "./test/__init__.py" ]