
run:
	sudo chmod -R 777 vol*
	sudo rm -rf ./vol-presta/var/cache/*
	docker-compose up

build:
	sudo chmod -R 777 vol*
	sudo rm -rf ./vol-presta/var/cache/*
	docker container prune -f
	docker-compose build
	sudo chmod -R 777 vol*
	docker-compose up --force-recreate

gitcleanallchanges:
	sudo chmod -R 777 vol*
	git clean -f -d
	git restore .

