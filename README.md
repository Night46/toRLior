toRLior is a colleciton of python classes that can be used to cerate a SOCKS5 based connection to TOR and it's client ControlPort.
It'sbuilt with python 2.7 and requires no additional installations besides the TOR client.

PREREQUISITES
- tor config file 'torrc' default location /usr/local/etc/tor
- set the tor config to allow SocksPort on port 9999
- set the tor config to allow ControlPort on port 9991
- set the tor config to allow HashedControlPassword
- set the ControlPort password to toRLior (via CLI tor --hash-password toRLior)
- set the ControlPort hash in your 'torrc' file to 16:4C46EEA1DBCFB4C96047FE8342A4C19120C5A493962943EC0F486FFC69
