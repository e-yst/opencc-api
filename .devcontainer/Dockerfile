FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

COPY requirements/*.txt /tmp/pip-requirements/

RUN apt-get update \
  && apt-get install -y --no-install-recommends opencc bash-completion \
  && pip3 install -U pip -r /tmp/pip-requirements/dev.txt