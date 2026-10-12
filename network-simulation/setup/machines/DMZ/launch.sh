podman build -t pyth-server machines/DMZ

# 2. On relance le conteneur
podman run -d --replace --name server-WEB --rm --ip 192.168.53.2 --cap-add=NET_ADMIN   --network sim-front-network pyth-server

