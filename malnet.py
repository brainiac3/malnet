#!/opt/local/bin/python
#
# MalNET v0.1
# brainiac3 <brainiac3@evilnerds.net>
#
# MalNET serves as a low interaction http server for tracking malware via http requests in an 
# environment. for this to work the domains hosting the malware need a dummy dns zone created 
# redirecting them to your host running MalNET. once MalNET has been started, you will see log 
# output to stderr and also created in the log file malnet.log. The log output will
# look as follows:
#
# Started Malnet HTTP Server...
# hostpc.domain.net [19/Dec/2010 11:34:21] Host: ['some.malwaredomain.com'] "GET / HTTP/1.1" 200 -
# ^ visiting host   ^ date                         ^malware domain visited  ^ request
#
# Usage:
# sudo python ./malnet.py <port>
#
# <port> defaults to port 80 if none specified
#

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import re, sys

class MalNETHandler(BaseHTTPRequestHandler):
	def do_GET(self):
        	self.send_response(200)
        	self.send_header("Content-type", "text/html")
        	self.end_headers()
        	self.wfile.write('<html></html>')

	def do_HEAD(self):
		return

	def log_message(self, format, *args):
		vhost = re.findall('Host: (.*?)\r\n',str(self.headers))
		sys.stdout = open('malnet.log', 'a') 
		sys.stdout.write("%s [%s] Host: %s %s\n" % 
			(self.address_string(), self.log_date_time_string(), vhost, format%args))
		sys.stderr.write("%s [%s] Host: %s %s\n" % 
			(self.address_string(), self.log_date_time_string(), vhost, format%args))

if __name__ == "__main__":
	try:
    		if sys.argv[1:]:
        		port = int(sys.argv[1])
    		else:
        		port = 80
	
        	server = HTTPServer(("", port), MalNETHandler)
        	print "[x] Started MalNET HTTP Server"
		print "[x] Hit Ctrl+C to exit"
        	server.serve_forever()
    	except KeyboardInterrupt:
        	print "\n[x] Interrupt received, shutting down MalNET server"
        	server.socket.close()
