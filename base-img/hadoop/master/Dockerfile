# VERSION 1.0
FROM java:openjdk-7
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

USER root

# Install Prerequisites of Packages.
# Supervisor Provides The Supervisor Daemon. See https://docs.docker.com/engine/admin/using_supervisord/
RUN apt-get install -y \
        rsync \
        ssh \
        supervisor \
        vim \
        wget

# Fix "Missing privilege separation directory: /var/run/sshd"
# when execute "/usr/sbin/sshd -D"
RUN mkdir /var/run/sshd

WORKDIR /usr/local

ENV HADOOP_VERSION 2.6.4
RUN mkdir hadoop \
    && curl -fsSL http://apache.claz.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz \
        | tar -xzC hadoop --strip-components=1

# See All "HADOOP_*" env variable in libexec/hadoop-config.cmd 
ENV HADOOP_HOME /usr/local/hadoop

ENV PATH $HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH

# Although $JAVA_HOME has been set, explicitly defind in 'hadoop-env.sh' is required.
RUN sed -i -- 's@${JAVA_HOME}@'"$JAVA_HOME"'@g' $HADOOP_HOME/etc/hadoop/hadoop-env.sh

# Add Configuration Files
COPY etc $HADOOP_HOME/etc/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Setup Passphraseless ssh And
# Automatically Add New Host Keys to The $HOME/.ssh/known_hosts File
RUN ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa \
    && cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys \
    && chmod 0600 ~/.ssh/authorized_keys
ENV HADOOP_SSH_OPTS -o StrictHostKeyChecking=no

# Port for web interface of the NameNode.
# By default it is available at:
#     NameNode - http://localhost:50070/
EXPOSE 50070

# Port for web interface of the ResourceManager.
# By default it is available at:
#     ResourceManager - http://localhost:8088/
EXPOSE 8088

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/bin/supervisord"]
