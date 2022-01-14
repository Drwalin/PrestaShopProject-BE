
REPO="127.0.0.1:5000"
IMAGE_NAME="hopbyteteamprestashopimage"

# sudo openvpn --config /etc/openvpn/vpnWETI.ovpn
# # postgresql:
# ssh -L 5432:actina15.maas:5432 rsww@172.20.83.101
# # docker image repo:
# ssh -L 5000:actina15.maas:5000 rsww@172.20.83.101
# postgresql://be_180109_prestashop:jhd4ever@localhost:5432/be_180109_prestadb

nothing:
	echo "Nothing done."

image:
	echo "Building image."
	docker build . -t $(IMAGE_NAME)
	docker push $(REPO)/$(IMAGE_NAME)
	echo "Image built and sent."

