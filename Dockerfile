FROM node:18-alpine AS frontend

COPY ./opencc-quasar /tmp/opencc-quasar

RUN cd /tmp/opencc-quasar/ \
  && yarn global add @quasar/cli \
  && yarn \
  && quasar build


FROM python:3.12-alpine

COPY . /opencc-api
COPY --from=frontend /tmp/opencc-quasar/dist/spa /opencc-api/app/static
COPY requirements /tmp/pip-requirements
RUN apk add opencc \
  && ln -vs /usr/lib/libopencc.so.1.1.7 /usr/lib/libopencc.so.1 \
  && pip install -U pip \
  && pip install -r /tmp/pip-requirements/base.txt

WORKDIR /opencc-api

EXPOSE 8000
CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0" ]