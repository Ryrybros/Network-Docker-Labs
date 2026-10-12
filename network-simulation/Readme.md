This is a Docker Lab to simulate a network.

This network has the following topology : 


The idea was to simulate a professionnal network architecure with a web server that is widely accessible, an internal access to internet and heavily controlled access to more sensistive data / services as the internal Database etc...

By default, all server containers  run a simple python http server, it is a way to simulate the the access to them when it is allowed by the firewall.

It is possible to inspect the traffic that the firewall is managing in real time using wireshark by running the 
debug/show-firewall 
file. 

This network can be re-setup (managing subnetworks mutual access) by changing the firewall rules.

Each subnet is physically connected to the firewall-router (the border beeing another subnet with the border firewall alone). They are logically connected or isolated to one another by the firewall.
