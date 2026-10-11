FROM almalinux:9
RUN dnf install -y --allowerasing \
    iproute \
    iputils \
    iptables \
    nftables \
    net-tools \
    procps-ng \
    tcpdump	\
    && dnf clean all
CMD ["/sbin/init"]

