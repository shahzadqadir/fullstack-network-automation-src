FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3.10
RUN apt-get install -y net-tools iputils-ping
RUN apt-get install -y python3-pip
RUN pip install paramiko ansible ansible-pylibssh
RUN apt-get install -y openssh-client vim

RUN useradd -ms /bin/bash script
RUN mkdir /home/script/.ssh
COPY cisco_ssh /home/script/.ssh/config
RUN chown -R script:script /home/script/.ssh

USER script
RUN chmod 700 /home/script/.ssh
RUN touch /home/script/.ssh/known_hosts
RUN chmod 644 /home/script/.ssh/known_hosts

WORKDIR /automation
