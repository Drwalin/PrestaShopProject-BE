# !/bin/bash

#sudo docker image rm 10.40.71.55:5000/hopbyteteamprestashopimage -f

cd context-presta
sudo docker build . -t 10.40.71.55:5000/hopbyteteamprestashopimage
sudo docker push 10.40.71.55:5000/hopbyteteamprestashopimage
cd ..

sudo docker stack deploy -c docker-compose.yml BE_180109 --with-registry-auth 
sudo docker service update BE_180109_be_180109_prestashop --force

