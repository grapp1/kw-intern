#!/bin/bash
## ParFlow install script for Ubuntu (Part 1 of 2)
## installing necessary packages in Ubuntu - need root privileges

apt-get update
export DEBIAN_FRONTEND=noninteractive

ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
apt-get install -y tzdata
dpkg-reconfigure --frontend noninteractive tzdata
apt-get install -y \
      build-essential \
      curl \
      git \
        gfortran \
        libopenblas-dev \
        liblapack-dev \
        openssh-client \
        openssh-server \
        openmpi-bin \
        libopenmpi-dev \
        tcl-dev \
        tk-dev
