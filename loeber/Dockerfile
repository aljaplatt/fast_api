# Dockerfile - blueprint for building images
# Image - Template for running containers
# Container - Running process containing packaged project

# specify base image 
FROM python:3.9.15-slim-bullseye

# add file into container - source, destination 
ADD main.py .

# install dependencies 
RUN pipenv install fastapi typing 



