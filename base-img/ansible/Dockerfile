# VERSION 1.3

FROM ubuntu
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

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
