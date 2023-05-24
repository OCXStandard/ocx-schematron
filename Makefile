# Project make file
# A self-documenting Makefile
# You can set these variables from the command line, and also
# from the environment for the first two.
SOURCE = ./resources
CONDA_ENV = schematron


# CONDA TASKS ##################################################################
# PROJECT setup using conda and powershell

conda-create:  ## Create a new conda environment with the python version and basic development tools
	@conda env create -f environment.yml
	@conda activate $(CONDA_ENV)

conda-upd:   ## Update the conda development environment when environment.yaml has changed
	@conda env update -f environment.yml

.PHONY: conda-create, conda-upd


# DOCKER TASKS ##################################################################

build:   ## Build the docker Schematron image using Dockerfile including the defined  resources
	@docker build . --tag ocx-validator:latest

run:  ## Run the docker image
	@docker stop schematron
	@docker rm schematron
	#@docker run -d --name schematron -p 8080:8080 -v ${PWD}/resources:/validator/resources/ -e validator.resourceRoot=/validator/resources/ isaitb/xml-validator
	@docker run -d --name schematron -p 8080:8080 -v ${PWD}/resources:/validator/resources/ ocx-validator

test-rudder: ## Access the Rudder upload page for validating ocx-rudder-extension v1.0.0 models

	@cmd /c start "http://localhost:8080/rudder/upload"

test-ocx: ## Access the OCX upload page for validating OCX v2.8.6 models

	@cmd /c start "http://localhost:8080/ocx/upload"
.PHONY: build, run, test-rudder, test-ocx


# HELP ########################################################################


.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

#-----------------------------------------------------------------------------------------------
