# Sockets Python Example
This code demonstrates a TCP client `tcp_client.py` which communicates with a TCP server `tcp_server.py`. The code was tested by connecting two laptops with each other and running either of the two programs on each laptop. The network settings on the laptop are as follows:

Laptop 1 (Server)
* IP : `192.168.0.1`
* Subnet-Prefix-Length : 24
* Gateway : `192.168.0.255`
* Preferred DNS : < EMPTY >
* Alternate DNS : < EMPTY >

Laptop 2 (Client)
* IP : `192.168.0.2`
* Subnet-Prefix-Length : 24
* Gateway : `192.168.0.255`
* Preferred DNS : < EMPTY >
* Alternate DNS : < EMPTY >

The choice of the gateway is arbitrary since no gateway is present in the LAN.
It is important that on the server side code, the server address is defined as `server_address = ('192.168.0.1', 9878)`. `server_address = ('localhost', 9878)` will not work because the server only accepts TCP
requests on from the IP `localhost` in this case (e.g. TCP requests from processes which run on the server).
