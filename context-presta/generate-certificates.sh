
openssl genrsa -out ssl/rootca.key 2048
echo 'Generate ROOT CA certificate:'
openssl req -x509 -new -nodes -key ssl/rootca.key -days 365 -out ssl/rootca.crt
openssl genrsa -out ssl/e-trojkat.key 2048
echo 'Generate E-trójkąt certificate:'
openssl req -new -key ssl/e-trojkat.key -out ssl/e-trojkat.csr
openssl x509 -req -in ssl/e-trojkat.csr -CA ssl/rootca.crt -CAkey ssl/rootca.key -CAcreateserial -out ssl/e-trojkat.crt -days 365

