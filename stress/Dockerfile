FROM quay.io/centos/centos:stream9

LABEL \
        author="Simone Tiraboschi" \
        email="stirabos@redhat.com" \
        version="0.0.1" \
        description="stress-ng in a container"

ENV SHELL=/bin/bash

RUN \
  dnf clean all && \
  dnf install -y epel-release && \
  dnf install -y libaio libbsd wget stress-ng && \
  dnf clean all

ENTRYPOINT ["/usr/bin/stress-ng"]
