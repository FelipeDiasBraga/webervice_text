#!/bin/bash
docker-compose down --rmi all
docker-compose build
docker-compose up