
build:
	docker-compose build
	docker-compose up --force-recreate

run:
	sudo chmod -R 777 vol*
	sudo rm -rf ./vol-presta/var/cache/*
	docker-compose up
	sudo chmod -R 777 vol*

build-old:
	sudo chmod -R 777 vol*
	sudo rm -rf ./vol-presta/var/cache/*
	docker container prune -f
	docker-compose build
	sudo chmod -R 777 vol*
	docker-compose up --force-recreate
	sudo chmod -R 777 vol*

gitcleanallchanges:
	sudo chmod -R 777 vol*
	git clean -f -d
	git restore .

