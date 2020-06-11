FROM nansencenter/geospaas:latest
LABEL purpose="ADAS viewer for Django-Geo-SpaaS"
ENV PYTHONUNBUFFERED=1

# Install Django-rest-framework

WORKDIR /src
