
# sudo openvpn --config /etc/openvpn/vpnWETI.ovpn
# # postgresql:
# ssh -L 5432:actina15.maas:5432 rsww@172.20.83.101
# # docker image repo:
# ssh -L 5000:actina15.maas:5000 rsww@172.20.83.101
# postgresql://be_180109_prestashop:jhd4ever@localhost:5432/be_180109_prestadb

nothing:
	echo "Nothing done."




run:
	sudo chmod -R 777 vol*
	sudo rm -rf ./vol-presta/var/cache/*
	docker-compose up
	sudo chmod -R 777 vol*

build:
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

