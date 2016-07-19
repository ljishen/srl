# VERSION 1.1

FROM maven:3-jdk-7

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

RUN apt-get update \
    && apt-get install -y \
        git \
        ssh \
        rsync

WORKDIR /root

ENV HADOOP_VERSION 2.7.2
http://download.nextag.com/apache/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz

ENV SPARK_VERSION 1.6.2
RUN mkdir spark \
    && curl -fsSL http://www.gtlib.gatech.edu/pub/apache/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop2.6.tgz \
        | tar -xzC spark --strip-components=1
ENV SPARK_HOME /root/spark
ENV PATH $SPARK_HOME/bin:$PATH

RUN git clone https://github.com/bigdatagenomics/adam.git
ENV MAVEN_OPTS -Xmx512m
ENV ADAM_HOME /root/adam
ENV PATH $ADAM_HOME/bin:$PATH
RUN mvn -f $ADAM_HOME clean package -DskipTests
RUN echo 'alias adam-submit="${ADAM_HOME}/bin/adam-submit"' >> ~/.bashrc \
    && echo 'alias adam-shell="${ADAM_HOME}/bin/adam-shell"' >> ~/.bashrc

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["adam-submit"]
