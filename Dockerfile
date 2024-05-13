FROM ubuntu:latest
LABEL authors="i.ilyin"

ENTRYPOINT ["top", "-b"]