FROM isaitb/xml-validator:latest
COPY resources /validator/resources/
ENV validator.resourceRoot /validator/resources/