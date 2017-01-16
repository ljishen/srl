# VERSION 1.5

FROM phusion/baseimage:0.9.19
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# rsync is required by ansible synchronize module
# python-netaddr is required by Jinja2 ipaddr filter
RUN apt-get update \
    && apt-get install -y \
        python-dev \
        python-pip \
        libssl-dev \
        libffi-dev \
        rsync \
        python-netaddr

RUN pip install cryptography ansible==2.1.3.0

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Ansible default config file
RUN mkdir -p /etc/ansible
COPY ansible.cfg /etc/ansible/

# Install Ansible default inventory file
RUN mkdir -p /root/ansible \
    && echo "[local]\nlocalhost ansible_connection=local" > /root/ansible/hosts
WORKDIR /root/ansible

# Use baseimage-docker's init system.
ENTRYPOINT ["/sbin/my_init", "--skip-startup-files", "--quiet", "--"]

CMD ["ansible-playbook", "--version"]
