echo "**** Generating private & public key ****"
set -e

openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:prime256v1 -out privkey-A.pem;

openssl pkey -in privkey-A.pem -pubout -out pubkey-A.pem;

echo "**** Finished generation ****"



echo "**** CSR ****" 

openssl req -x509 -new -nodes -key privkey-A.pem -sha256 -days 1024 \
    -subj "/CN=serverA.internal" \
    -out serverA.crt