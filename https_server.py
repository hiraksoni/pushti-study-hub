import http.server
import ssl
import os
import sys

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PORT = 8443

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

def run():
    server_address = ('0.0.0.0', PORT)
    httpd = http.server.HTTPServer(server_address, Handler)
    
    cert_file = os.path.join(DIRECTORY, 'localhost.crt')
    key_file = os.path.join(DIRECTORY, 'localhost.key')
    
    if not (os.path.exists(cert_file) and os.path.exists(key_file)):
        from werkzeug.serving import make_ssl_devcert
        make_ssl_devcert(os.path.join(DIRECTORY, 'localhost'), host='localhost')
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print(f"[SUCCESS] Pushti Study Hub HTTPS server running at: https://localhost:{PORT}/")
    print(f"[DIRECTORY] {DIRECTORY}")
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == '__main__':
    run()
