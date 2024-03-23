################################################################################
#                                  Variables                                   #
################################################################################

.PHONY: help
.DEFAULT_GOAL := help

# Target OS detection
ifeq ($(OS),Windows_NT) # OS is a preexisting environment variable on Windows
	OS = windows
else
	UNAME := $(shell uname -s)
	ifeq ($(UNAME),Darwin)
		OS = macos
	else ifeq ($(UNAME),Linux)
		OS = linux
	else
    	$(error OS not supported by this Makefile)
	endif
endif

################################################################################
#                                  Commands                                    #
################################################################################

test: ## Test function for random changes
	@echo 'Operating System: ${OS}'

install: ## Create a virtual environment prior to running this command
# python -m venv venv/
# source venv/bin/activate
	pip install -r requirements.txt

run: ## Runs the full play pong pipeline
# linux
	python play.py -r 1 -m 2
# windows
# cd C:\repos\github\pong-ai
# pip install -r requirements.txt
# .\play.ps1

################################################################################
#                            Functions and Helpers                             #
################################################################################

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
