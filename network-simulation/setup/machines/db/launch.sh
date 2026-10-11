podman build -t pyth-server machines/db

# 2. On relance le conteneur
podman run -d --replace --name server-DB --rm --cap-add=NET_ADMIN  --network sim-back-network pyth-server 
