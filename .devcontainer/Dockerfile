# syntax=docker/dockerfile:1
ARG PYTHON_VER=3.12
FROM python:${PYTHON_VER}-alpine
RUN apk upgrade && \
    apk add --no-cache git
RUN pip install --no-cache-dir "fastapi[standard]"
