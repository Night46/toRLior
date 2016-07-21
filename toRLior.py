# ##################################################################################################################
# PREREQUISITES
# - tor config file 'torrc' default location /usr/local/etc/tor
# - set the tor config to allow SocksPort on port 9999
# - set the tor config to allow ControlPort on port 9991
# - set the tor config to allow HashedControlPassword
# - set the ControlPort password to toRLior (via CLI tor --hash-password toRLior)
# - set the ControlPort hash in your 'torrc' file to 16:4C46EEA1DBCFB4C96047FE8342A4C19120C5A493962943EC0F486FFC69
# ##################################################################################################################

import threading
import socket
import socks
import urllib
import Queue
import time
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
    self.dest_socket = "('my-ip.herokuapp.com', 80)"
      # destination address and destination port
    self.test_count = 3
      # number of times to run the conneciton test function
    self.post_dest = 'http://my-ip.herokuapp.com'
      # destination address for tor_post
    self.post_data = {'A': 'A'}
      # data to be sent as the POST
    self.get_dest = 'http://my-ip.herokuapp.com'
      # # destination address for tor_get
    self.post_data_encode = urllib.urlencode(self.post_data)
      # urllib encoded representation of post_data
    self.post_headers = {
      'Host': 'my-ip.herokuapp.com',
      'Connection': 'keep-alive',
      'Cache-Control': 'max-age=0',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.49 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Encoding': 'gzip, deflate, sdch',
      'Accept-Language': 'en-US,en;q=0.8,he;q=0.6',
      'DNT': '1'
      }
    self.thread_dest = 'http://my-ip.herokuapp.com'
      # threaded sockets destination address
    self.thread_count = 5
      # the number of itterations
    self.c = socket.socket()
      # TCP socket for raw data
    self.s = socks.setdefaultproxy(self.proxy_type, self.proxy_ip, self.proxy_port)
      # set TOR proxy
    self.sp = socks.socksocket()
      # SPCKS socket
    self.sp.setproxy(self.proxy_type, self.control_ip, self.control_port, self.rdns, self.c_username, self.c_passwd)
      # set TOR ControlPort proxy
    self.ip_regex = re.compile(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
      # regex search for an IP address


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

  def tor_get(self):
    import urllib2
    request = urllib2.Request(self.get_dest)
    open_url = urllib2.urlopen(request)
    raw_data = open_url.read()
    print raw_data

  def tor_post(self):
    import urllib2
    request = urllib2.Request(self.post_dest, self.post_data_encode, self.post_headers)
    open_url = urllib2.urlopen(request)
    raw_data = open_url.read()
    ip = self.ip_regex.search(raw_data)
    print ip.group()

  def send_close(self):
    self.s.close()


class multi_thread(toRLior, threading.Thread):
  def tor_thread_connect(self):
    self.s
    socket.socket = socks.socksocket

  def threaded_get(self):
    import urllib2
    for i in range (self.thread_count):
      request = urllib2.Request(self.thread_dest)
      open_url = urllib2.urlopen(request)
      raw_data = open_url.read()
      print raw_data


  def threaded_get_changeIP(self):
    import urllib2
    for i in range (self.thread_count):
      request = urllib2.Request(self.thread_dest)
      open_url = urllib2.urlopen(request)
      raw_data = open_url.read()
      print raw_data
      if i < 1:
        torcontrol = controller()
        torcontrol.control_connect(('127.0.0.1', 9991))
        print 'asking for a new_circuit..'
        torcontrol.new_circuit()
      elif i < self.thread_count-1 :
        print 'waiting for 15s before ciruit change..'
        time.sleep(15)
        torcontrol = controller()
        torcontrol.control_connect(('127.0.0.1', 9991))
        print 'asking for a new_circuit..'
        torcontrol.new_circuit()

      i = i+1
      

  def threaded_post(self):
    import urllib2
    for i in range (self.thread_count):
      request = urllib2.Request(self.post_dest, self.post_data_encode, self.post_headers)
      open_url = urllib2.urlopen(request)
      raw_data = open_url.read()
      print raw_data

  def threaded_post_changeIP(self):
    import urllib2
    for i in range (self.thread_count):
      request = urllib2.Request(self.post_dest, self.post_data_encode, self.post_headers)
      open_url = urllib2.urlopen(request)
      raw_data = open_url.read()
      print raw_data
      if i < 1:
        torcontrol = controller()
        torcontrol.control_connect(('127.0.0.1', 9991))
        print 'asking for a new_circuit..'
        torcontrol.new_circuit()
      elif i < self.thread_count-1 :
        print 'waiting for 15s before ciruit change..'
        time.sleep(15)
        torcontrol = controller()
        torcontrol.control_connect(('127.0.0.1', 9991))
        print 'asking for a new_circuit..'
        torcontrol.new_circuit()

      i = i+1

  def send_thread_close(self):
    self.s.close()


class controller(toRLior):
  def control_connect(self, control_socket):
    self.sp.setproxy()
    self.sp.connect(control_socket)
    self.sp.send('AUTHENTICATE "toRLior"\r\n')
    

  def new_circuit(self):
    self.sp.send('SIGNAL NEWNYM\r\n')
    self.sp.close()   

  def clear_dns_cache(self):
    self.sp.send('SIGNAL CLEARDNSCACHE\n\r')
    self.sp.close()

  def halt(self):
    self.sp.send('SIGNAL HALT\n\r')
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
# torconnect.tor_get()

# torconnect = connect()
# torconnect.tor_connect()
# torconnect.tor_post()

# torconnect = connect()
# torconnect.tor_connect()
# torconnect.tor_extern_ip()

# torthread = multi_thread()
# torthread.tor_thread_connect()
# torthread.threaded_get()

# torthread = multi_thread()
# torthread.tor_thread_connect()
# torthread.threaded_get_changeIP()

# torcontrol = controller()
# torcontrol.control_connect(('127.0.0.1', 9991))
# torcontrol.new_circuit()

# torcontrol = controller()
# torcontrol.control_connect(('127.0.0.1', 9991))
# torcontrol.clear_dns_cache()

# torcontrol = controller()
# torcontrol.control_connect(('127.0.0.1', 9991))
# torcontrol.halt()