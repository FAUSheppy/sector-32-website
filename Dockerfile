FROM python:3.8-slim-buster

RUN apt update
RUN apt install python3-pip git -y
RUN python3 -m pip install waitress
RUN python3 -m pip install --upgrade pip

RUN git clone https://github.com/FAUSheppy/sector-32-website /app
WORKDIR /app
RUN python3 -m pip install -r req.txt

HEALTHCHECK CMD --interval=5m --timeout=5s /usr/bin/curl http://localhost:5000/ || exit 1
EXPOSE 5000/tcp

RUN apt remove git -y
RUN apt autoremove -y
RUN which waitress-serve

CMD waitress-serve --host 0.0.0.0 --port 5000 --call 'app:createApp'
