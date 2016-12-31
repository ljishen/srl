# VERSION 1.4

FROM phusion/baseimage:0.9.19
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update \
    && apt-get install -y \
        python-dev \
        python-pip \
        libssl-dev \
        libffi-dev

RUN pip install cryptography ansible==2.1.3.0

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Ansible inventory file
RUN mkdir -p /etc/ansible \
    && echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

RUN mkdir -p /root/ansible
WORKDIR /root/ansible

CMD ["ansible-playbook", "--version"]
