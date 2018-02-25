FROM ubuntu:16.04

RUN apt-get update && apt-get -y install \
    git python3-dev python3-pip libleveldb-dev libssl-dev man vim

RUN git clone https://github.com/CityOfZion/neo-python.git

WORKDIR neo-python

RUN pip3 install -r requirements.txt

ADD protocol.privnet.json /neo-python/

CMD python3 prompt.py
