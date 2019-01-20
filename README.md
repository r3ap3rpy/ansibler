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

Python is needed for ansible to work so you should have at least a version 2.* on each system against which you work.

If you use a centos based machine perform these tasks before you do anything.

```bash
yum update 

yum install python python-devel ansible openssl
```

Steps to perform on each host for key based authentication.

```bash
adduser ansible
passwd ansible
```

Use the visudo to add passwordless sudo to the user. Look for the line root and add the folowing below.

```bash
visudo

ansible ALL=(ALL) NOPASSWD: ALL
```