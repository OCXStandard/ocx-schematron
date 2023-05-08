#!/bin/zsh

docker run -d --name schematron -p 8080:8080 \
             -v ${PWD}/resources:/validator/resources/ \
             -e validator.resourceRoot=/validator/resources/  \
             isaitb/xml-validator