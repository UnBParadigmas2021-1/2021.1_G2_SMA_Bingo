FROM victorcmoura/pade:paradigmas

WORKDIR /app

RUN pip3.7 install websockets

COPY . /app

CMD pade --config_file pade_config.json
