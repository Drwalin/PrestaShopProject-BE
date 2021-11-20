
run:
	docker-compose up

build:
	sudo chmod -R 777 vol*
	docker container prune -f
	docker-compose build
	sudo chmod -R 777 vol*
	docker-compose up --force-recreate

gitcleanallchanges:
	sudo chmod -R 777 vol*
	git clean -f -d
	git restore .

