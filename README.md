## Welcome

This repository provides you with sample playbooks for all sorts of things.

The playbooks were tested to run agains ubuntu, debian, and centos systems.

The basic setup consists of an ansible user for each systems.

You need to do the following to allow key based ssh authentication.

```bash
ssh-keygen 

ssh-copy-id ansible@target
```
Make sure you copy the key to the host itself too.
