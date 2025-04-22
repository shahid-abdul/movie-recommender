# movie-recommendation

# CICD-ML-PROJECT

## End to End MAchine Learning Project

1. Docker Build checked
2. Github Workflow
3. Iam User In AWS

## Building Docker Image

1. docker build -t shahidabdul/movie-recommendation-app .
2. docker run -p 8080:8080 shahidabdul/movie-recommendation-app
3. docker images
4. docker push shahidabdul/movie-recommendation-app:latest

## Docker Setup In EC2 commands to be Executed

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## Configure EC2 as self-hosted runner:

## Setup github secrets:

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION =

AWS_ECR_LOGIN_URI = 381492194707.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = movie-recommender
