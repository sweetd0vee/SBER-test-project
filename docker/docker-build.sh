#!/usr/bin/env bash

IMAGE=arina/sber
TAG=master

cd ..

docker build -t $IMAGE:$TAG .
