# This image is for CI testing purposes only
FROM python:3
# Installing Fluvio CLI for creating topics in example
RUN curl -fsS https://packages.fluvio.io/v1/install.sh | bash
ENV PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/.fluvio/bin
RUN pip install fluvio
COPY ./timekeeper.sh .
CMD /bin/bash ./timekeeper.sh 'hello world!'

COPY ./timekeeper-connector.sh .
COPY ./testfiles/catfact.yml ./catfact.yml
CMD /bin/bash -c './timekeeper-connector.sh "hello world"'

COPY ./timekeeper-full.sh .
COPY ./testfiles/catfact-module.yml ./catfact.yml
COPY ./testfiles/catfacts_map.wasm ./catfacts-map/target/wasm32-unknown-unknown/release/catfacts_map.wasm
CMD /bin/bash -c './timekeeper-full.sh "hello world"'
