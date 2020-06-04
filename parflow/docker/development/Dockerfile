# -----------------------------------------------------------------------------
# Dockerfile for building ParFlow image on Ubuntu
# -----------------------------------------------------------------------------
# Build options (* = default)
#
#  BASE_IMAGE
#    *  ubuntu:18.04
#       ubuntu:20.04
#
#  PARFLOW_VERSION
#    *  v3.6.0
#       master
#
#  HYPRE_VERSION
#    *  v2.19.0
#       master
#
# -----------------------------------------------------------------------------

ARG BASE_IMAGE=ubuntu:18.04
FROM ${BASE_IMAGE}

COPY ./scripts .
RUN ./scripts/01_packages.sh

RUN groupadd -g 1000 ubuntu && \
    useradd -u 1000 -g user -m -N -s /bin/bash ubuntu

USER ubuntu
WORKDIR /home/ubuntu/

ENV PARFLOW_BRANCH ${PARFLOW_VERSION}
ENV HYPRE_BRANCH ${HYPRE_VERSION}

RUN ./scripts/02_parflow.sh
