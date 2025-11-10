import http.server
import socketserver
import ssl
import json
PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        except:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        
        post_data = self.rfile.read(content_length)

        python_obj = json.loads(post_data)
        print(b"Data")
        print(python_obj)
        print(b"Age")
        print(python_obj["age"])
        print(f"Received POST data: {post_data.decode('utf-8')}")
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        response_message = b"POST request received successfully!"
        self.wfile.write(post_data)         
        self.wfile.write(response_message)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    '''
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        keyfile="key.pem",
        certfile="cert.pem",
        server_side=True
    )
    '''
    print(f"Serving at port {PORT}, ready to handle POST requests")
    httpd.serve_forever()
