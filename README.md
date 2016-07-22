* Overview

=toRLior= is a colleciton of python classes that can be used to cerate a SOCKS5 based connection to TOR and its client ControlPort.
It's built with python 2.7 and requires only =SocksiPy= installations besides a =TOR= client.


* Prerequisites

SocksiPy (can be downloaded at http://socksipy.sourceforge.net/)
tor config file 'torrc' default location /usr/local/etc/tor
set the tor config to allow SocksPort on port 9999
set the tor config to allow ControlPort on port 9991
set the tor config to allow HashedControlPassword
set the ControlPort password to toRLior (via CLI tor --hash-password toRLior)
set the ControlPort hash in your 'torrc' file to 16:4C46EEA1DBCFB4C96047FE8342A4C19120C5A493962943EC0F486FFC69


* USAGE

** The =connect= class

=torconnect.tor_connect()= :: | *=connects to the TOR client proxy SOCKS5 port=*
=torconnect.tor_extern_ip()= :: | *=prints out the IP address of the exit point=*
=torconnect.tor_get()= :: | *=connect to the remote destination and sends a GET request=*
=torconnect.tor_post()= :: | *=connect to the remote destination and sends a POST request=*
=torconnect.send_close()= :: | *=close the current session=*

** The =multi_thread= class

=torthread.tor_thread_connect()= :: | *=connects to the TOR client proxy SOCKS5 port=*
=torthread.threaded_get_run()= :: | *=connect to the remote destination and sends multi threaded GET requests=*
=torthread.threaded_get_changeIP()= :: | *=connect to the remote destination and sends multi threaded GET requests AND change circuit per request=*
=torthread.threaded_post_run()= :: | *=connect to the remote destination and sends multi threaded POST requests=*
=torthread.threaded_post_changeIP_run()= :: | *=connect to the remote destination and sends multi threaded POST requests AND change circuit per request=*
=torthread.send_thread_close()= :: | *=close the current session=*

** The =controller= class

=torcontrol.control_connect(('127.0.0.1', 9991))= :: | *=connects to the TOR client ControlPort=*
=torcontrol.new_circuit()= :: | *=sends a new circuit request to the TOR client ControlPort=*
=torcontrol.clear_dns_cache()= :: |  *=send a clear DNS cache request to the TOR client ControlPort=*
=torcontrol.halt()= :: | *=sends a disconnect request to the TOR client ControlPort=*

** The =test= class

=test.test_circuit_change()= :: | *=test the connection to TOR and change circuits=*