#!/bin/bash -e

passwd=''
if [ ${#1} -gt 4 ]; then
    passwd=$1
    echo "Generate SSH rsa key with passphrase ${passwd}."
else
    echo "WARNING: Generate SSH rsa key without passphrase (valid passphrase > 4 bytes)."
fi

ssh-keygen -qt rsa -N "$passwd" -f /root/.ssh/id_rsa
