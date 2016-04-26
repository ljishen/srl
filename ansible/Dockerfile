# VERSION 1.0

FROM ubuntu:latest

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# Install Prerequisites
RUN apt-get update \
    && apt-get install -y \
        python-pip \ 
        python-dev \
        git \
        vim \
        screen \
    && pip install --upgrade paramiko PyYAML Jinja2 httplib2 six

WORKDIR /opt

# Install Ansible From Source
RUN git clone git://github.com/ansible/ansible.git --recursive

WORKDIR /opt/ansible

# Compiling Ansible
RUN bash -c 'source ./hacking/env-setup'

# Clean Up
RUN rm -r /var/lib/apt/lists/* 

RUN mkdir -p /etc/ansible \
    && echo '[local]\nlocalhost\n' > /etc/ansible/hosts

# Disable Host Key Checking
# See http://docs.ansible.com/ansible/intro_getting_started.html#host-key-checking
ENV ANSIBLE_HOST_KEY_CHECKING False

ENV PATH /opt/ansible/bin:$PATH
ENV PYTHONPATH /opt/ansible/lib:$PYTHONPATH

# default command: display Ansible version
CMD [ "ansible-playbook", "--version" ]
