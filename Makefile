.PHONY: compose down test python mongo drop

MAKEPATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PWD := $(dir $(MAKEPATH))

compose:
	docker-compose up -d

down :
	docker stop python-api && docker rm python-api

test:
	docker exec python-api pytest -s

python:
	docker exec -it python-api bash

mongo:
	docker exec -it python-mongo-container mongo

drop :
	docker rmi python_python-api