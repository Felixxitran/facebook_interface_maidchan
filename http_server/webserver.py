from http.server import HTTPServer,BaseHTTPRequestHandler

class webHandler(BaseHTTPRequestHandler):
 def do_GET(self):
  self.send_response(200)
  self.send_header('content-type','text/html')
  self.end_headers()
  self.wfile.write('Hello Khoaa'.encode())

def main():
 PORT = 300
 server = HTTPServer(('',PORT),webHandler)
 print('run on port %s' %PORT)
 server.serve_forever()


if __name__ == '__main__':
 main()

