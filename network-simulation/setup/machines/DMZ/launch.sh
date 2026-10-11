podman build -t pyth-server machines/DMZ

# 2. On relance le conteneur
podman run -d --replace --name server-WEB --rm --cap-add=NET_ADMIN   --network sim-front-network pyth-server

