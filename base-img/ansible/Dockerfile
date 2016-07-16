# VERSION 1.2

FROM ubuntu:latest

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# Install Prerequisites
# Note: libffi-dev is required for paramiko
RUN apt-get update \
    && apt-get install -y \
        python-pip \
        libffi-dev \
        libssl-dev \
        sshpass \
        git \
    && pip install --upgrade pycrypto paramiko PyYAML Jinja2 httplib2 six

WORKDIR /opt

# Install Ansible From Source
ENV ANSIBLE_VERSION v2.0.2.0-1
RUN git clone git://github.com/ansible/ansible.git --recursive --branch $ANSIBLE_VERSION

WORKDIR /opt/ansible

# Compiling && Install Ansible
RUN bash -c 'source ./hacking/env-setup' \
    && make install

# Copy Default configuration file
RUN mkdir /etc/ansible \
    && cp examples/ansible.cfg /etc/ansible \
    && cp examples/hosts /etc/ansible

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["ansible-playbook", "--version"]
