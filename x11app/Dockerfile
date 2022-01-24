FROM ubuntu:latest
#ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq install -y xterm x11-apps 
CMD ['xclock']