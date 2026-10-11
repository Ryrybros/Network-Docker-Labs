#!/bin/bash
# Remove Podman's default gateway and point to the firewall container
ip route add default via 192.168.54.254

# Run the actual application
exec "$@"
