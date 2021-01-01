import http.server
import socketserver

# handler variable is going to handle the request of the client on the server
handler = http.server.SimpleHTTPRequestHandler


# let's define to start the server on port 8080
with socketserver.TCPServer(("", 8080), handler) as httpd:
    #let's keep the server running until getting request from client
    httpd.serve_forever()



