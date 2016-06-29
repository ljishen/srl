# VERSION 1.0

FROM ubuntu:latest

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        unzip \ 
        wget

ENV FOLDER_NAME interbench

WORKDIR /root
RUN wget https://github.com/Mustaavalkosta/interbench/archive/master.zip \
    && unzip master.zip \
    && rm master.zip \
    && mv interbench-master $FOLDER_NAME

RUN make -C $FOLDER_NAME

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir results
WORKDIR /root/results
ENTRYPOINT ["/bin/bash", "-c", "../$FOLDER_NAME/interbench"]
CMD ["-r", "-L", "1"]
