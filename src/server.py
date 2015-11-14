from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
 
port = 8000
class Tykkays20HTTPRequestHandler(BaseHTTPRequestHandler):
  
  #handle GET command
  def do_GET(self):
    try:
        self.send_response(200)
        self.send_header('Content-type','text-html')
        self.end_headers()
        self.wfile.write("<html><head><title>Title goes here.</title></head>")
        self.wfile.write("<body><p>Hello, world</p>")
        return
      
    except IOError:
      self.send_error(404, 'file not found')
  
def run():
  print('http server is starting...')
 
  #ip and port of servr
  #by default http server port is 80
  server_address = ('127.0.0.1', port)
  httpd = HTTPServer(server_address, Tykkays20HTTPRequestHandler)
  print('http server is running in port ' + str(port) + '...')
  httpd.serve_forever()
  
if __name__ == '__main__':
  run()
