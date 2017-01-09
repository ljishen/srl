# deploy-ceph-docker

## Usage
Install roles included in requirements.yml

```bash
ansible-galaxy install -r requirements.yml
```

Check the hosts file before you run this command

```bash
docker run --rm \
    --network=host \
    -v `pwd`:/root/ansible \
    -v /etc/ansible/roles:/etc/ansible/roles \
    -v `pwd`/log:/var/log \
    -v $HOME/.ssh:/root/.ssh \
    ljishen/ansible \
    ansible-playbook site.yml
```
