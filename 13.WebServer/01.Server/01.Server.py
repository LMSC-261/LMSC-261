# Run this program from terminal:
#   python3 1.Server.py

from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)

    self.send_header("Content-type", "text/html")
    self.end_headers()

    self.wfile.write(b"<!DOCTYPE html>")
    self.wfile.write(b"<html lang='en'>")
    self.wfile.write(b"<head>")
    self.wfile.write(b"<title>hello, title</title>")
    self.wfile.write(b"</head>")
    self.wfile.write(b"<body>")
    self.wfile.write(b"hello, body")
    self.wfile.write(b"</body>")
    self.wfile.write(b"</html>")

port = 80
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
httpd.serve_forever()

# Once the program is running, put the following URLs
# in the serach bar of your web browswer:
#
# http://127.0.0.1/
# localhost
#
# Above two means the same thing: 
# Loop back IP address to your computer