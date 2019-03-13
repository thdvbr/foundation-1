import http.server
import socketserver 

#CGIHTTPRequestHandler instead of SimpleHTTPRequestHandler
#allows python scripts to be called as an action (POST)

#define the handler to be the CGI server
handler = http.server.CGIHTTPRequestHandler

#point the handler to a directory with scripts
handler.cgi_directories = ["/scripts"]

#define the server using the handler 
PORT = 8000
httpd = socketserver.TCPServer(("localhost", PORT), handler)

#set variables which the CGIHTTPRequestHandler expects
httpd.server_name = "myServer"
httpd.server_port = PORT 

print("Starting CGI server at http://127.0.0.1:8000")

#run the server, to kill it, issue ctrl+c
httpd.serve_forever()