  
FROM nansencenter/geospaas:latest
LABEL purpose="Adas viewer for Django-Geo-SpaaS"
ENV PYTHONUNBUFFERED=1

# Install Django-rest-framework
# RUN pip install djangorestframework markdown django-filter 

WORKDIR /src