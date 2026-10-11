#!/bin/bash
# Remove Podman's default gateway and point to the firewall container
set -e
ip route add default via 192.168.52.254

# Run the actual application
exec "$@"
