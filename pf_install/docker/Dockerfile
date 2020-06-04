# Dockerfile for building ParFlow image on Ubuntu
#
# -----------------------------------------------------------------------------
# Build options (* = default)
# -----------------------------------------------------------------------------
#
#  BASE_IMAGE
#    *  ubuntu:18.04
#
#  Downloads ParFlow version 3.6.0
# -----------------------------------------------------------------------------


ARG BASE_IMAGE=ubuntu:18.04
FROM ${BASE_IMAGE}

COPY ./pf_install_packages.sh .
RUN ./pf_install_packages.sh

RUN groupadd -g 1000 user && \
    useradd -u 1000 -g user -m -N -s /bin/bash user

USER user
WORKDIR /home/user/

COPY ./pf_install.sh .
RUN ./pf_install.sh
