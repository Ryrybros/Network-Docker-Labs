podman build -t pyth-server machines/accounting

# 2. On relance le conteneur
podman run -d --replace --name server-accounting --rm --cap-add=NET_ADMIN   --network sim-third-network pyth-server

