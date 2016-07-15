# ##################################################################################################################
# PREREQUISITES
# - tor config file 'torrc' default location /usr/local/etc/tor
# - set the tor config to allow SocksPort on port 9999
# - set the tor config to allow ControlPort on port 9991
# - set the tor config to allow HashedControlPassword
# - set the ControlPort password to toRLior (via CLI tor --hash-password toRLior)
# - set the ControlPort hash in your 'torrc' file to 16:4C46EEA1DBCFB4C96047FE8342A4C19120C5A493962943EC0F486FFC69
# ##################################################################################################################

import socket
import socks
import threading
import time
import select
import sys
import re



class toRLior:
  def __init__(self):
    self.proxy_ip = '127.0.0.1'
      # IP address or DNS for the proxy server
    self.proxy_port = 9999
      # proxy port Default is 1080 for socks and 8080 for http
    self.proxy_type = socks.PROXY_TYPE_SOCKS5
      # PROXY_TYPE_SOCKS4, PROXY_TYPE_SOCKS5 and PROXY_TYPE_HTTP
    self.control_ip = '127.0.0.1'
      # the control ip address
    self.control_port = 9991
      # the control port
    self.control_socket = "('127.0.0.1', 9991)"
      # the socket for tor control
    self.check_ip = 'http://my-ip.herokuapp.com'
      # returns the external ip address
    self.rdns = True
      # DNS resolving remotely, False, DNS resolving locally
    self.username = None
      # Socks5, username / password authentication; Socks4 servers, be sent as the userid HTTP server parameter is ignored
    self.passwd = None
      # only for Socks5
    self.c_username = 'user'
      # control port user
    self.c_passwd = 'pass'
      # control port pass
    self.Dest_socket = "('my-ip.herokuapp.com', 80)"
      # destination address and destination port
    self.test_count = 3
      # number of times to run the conneciton test function
    self.headers = 'headers'
    self.threads = []

    self.s = socks.setdefaultproxy(self.proxy_type, self.proxy_ip, self.proxy_port)
    
    self.sp = socks.socksocket()
    self.sp.setproxy(self.proxy_type, self.control_ip, self.control_port, self.rdns, self.c_username, self.c_passwd)

    self.ip_regex = re.compile(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')


class connect(toRLior):
  def tor_connect(self):
    self.s
    socket.socket = socks.socksocket

  def tor_extern_ip(self):
    import urllib2
    request = urllib2.Request(self.check_ip)
    open_url = urllib2.urlopen(request)
    raw_data = open_url.read()
    ip = self.ip_regex.search(raw_data)
    print ip.group()

  def send_raw(self, data):
    self.s.send(data)
    self.s.send(self.headers)

  def send_close(self):
    self.s.close()

class controller(toRLior):
  def control_connect(self, control_socket):
    self.sp.setproxy()
    self.sp.connect(control_socket)
    self.sp.send('AUTHENTICATE "toRLior"\r\n')
    

  def new_circuit(self):
    self.sp.send('SIGNAL NEWNYM\r\n')
    self.sp.close()

  def halt(self):
    self.sp.send('SIGNAL HALT\n\r')
    self.sp.close()    

  def clear_dns_cache(self):
    self.sp.send('SIGNAL CLEARDNSCACHE\n\r')
    self.sp.close()


class test(toRLior):
  def test_circuit_change(self):
    for i in range(self.test_count):
      print ''
      torconnect = connect()
      torconnect.tor_connect()
      print 'tor_extern_ip -'+str(i+1)+'-'
      torconnect.tor_extern_ip()
      print ''

      if i < 1:
        torcontrol = controller()
        torcontrol.control_connect(('127.0.0.1', 9991))
        print 'asking for a new_circuit..'
        torcontrol.new_circuit()
      elif i < self.test_count-1 :
        print 'waiting for 15s before ciruit change..'
        time.sleep(15)
        torcontrol = controller()
        torcontrol.control_connect(('127.0.0.1', 9991))
        print 'asking for a new_circuit..'
        torcontrol.new_circuit()

      i = i+1


# ##################################### #
# uncomment below to test functionality #
# ##################################### #
# print 'test'
# debug = test()
# debug.test_circuit_change()

# torconnect = connect()
# torconnect.tor_connect()
# torconnect.tor_extern_ip()

# torcontrol = controller()
# torcontrol.control_connect(('127.0.0.1', 9991))
# torcontrol.new_circuit()

# torcontrol = controller()
# torcontrol.control_connect(('127.0.0.1', 9991))
# torcontrol.clear_dns_cache()

# torcontrol = controller()
# torcontrol.control_connect(('127.0.0.1', 9991))
# torcontrol.halt()