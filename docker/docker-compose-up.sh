#!/bin/bash


export COMPOSE_PROJECT_NAME=sber

docker-compose -f docker-compose.yml up -d
