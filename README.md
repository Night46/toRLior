toRLior is a colleciton of python classes that can be used to cerate a SOCKS5 based connection to TOR and it's client ControlPort.
It's built with python 2.7 and requires no additional installations besides the TOR client.


PREREQUISITES
- tor config file 'torrc' default location /usr/local/etc/tor
- set the tor config to allow SocksPort on port 9999
- set the tor config to allow ControlPort on port 9991
- set the tor config to allow HashedControlPassword
- set the ControlPort password to toRLior (via CLI tor --hash-password toRLior)
- set the ControlPort hash in your 'torrc' file to 16:4C46EEA1DBCFB4C96047FE8342A4C19120C5A493962943EC0F486FFC69


USAGE
- torconnect.tor_connect()
	connects to the TOR client proxy SOCKS5 port
- torconnect.tor_extern_ip()
	prints out the IP address of the exit point


- torcontrol.control_connect(('127.0.0.1', 9991))
	connects to the TOR client ControlPort
- torcontrol.new_circuit()
	sends a new circuit request to the TOR client ControlPort
- torcontrol.clear_dns_cache()
	send a clear DNS cache request to the TOR client ControlPort
- torcontrol.halt()
	sends a disconnect request to the TOR client ControlPort
