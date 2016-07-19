#!/bin/bash -e


# Starting OpenBSD Secure Shell server: sshd 
service ssh start

# Format the filesystem
hdfs namenode -format

# Start NameNode daemon and DataNode daemon
start-dfs.sh

# Make the HDFS directories required to execute MapReduce jobs
hdfs dfs -mkdir /user \
    && hdfs dfs -mkdir /user/`whoami`

# Start ResourceManager daemon and NodeManager daemon
start-yarn.sh
