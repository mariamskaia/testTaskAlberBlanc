FROM --platform=linux/amd64 ubuntu:23.04
WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install -y python3 python3-venv
RUN python3 -m venv /root/py
RUN /root/py/bin/pip3 install pytest websockets pytest-asyncio
