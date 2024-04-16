# SampleFlaskApp is a web app created using flask web framework written in Python. 

A docker image for the flask application is created using the Dockerfile with the following command: 
docker build sampleflaskapp

A docker container can be created using docker image with the command:  docker run -p 5000:5000 sampleflaskapp

Detailed steps for generating the docker image and pushing to Docker Hub are available at https://thetechdarts.com/dockerize-a-python-flask-app-and-push-to-docker-hub/
