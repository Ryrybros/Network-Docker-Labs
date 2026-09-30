podman build -t pyth-server .

# 2. On relance le conteneur
podman run -it --replace --name server --network snmp-network pyth-server

