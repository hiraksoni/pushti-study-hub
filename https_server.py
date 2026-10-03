# -*- coding: utf-8 -*-
"""
Pushti Study Hub - Dual Protocol Local Server (HTTPS & HTTP)
Serves the Study Hub over both:
  - HTTPS on port 8443 (https://localhost:8443/)
  - HTTP  on port 8000 (http://localhost:8000/)
Multi-threaded, CORS-enabled, auto-generating development SSL certificate.
"""

import http.server
import ssl
import os
import sys
import threading
import time

# Ensure safe UTF-8 printing across Windows consoles (cp1252 workaround)
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
HTTPS_PORT = 8443
HTTP_PORT = 8000

class HubRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        if self.path.startswith('/api/tts'):
            import urllib.parse
            import urllib.request
            parsed = urllib.parse.urlparse(self.path)
            qs = urllib.parse.parse_qs(parsed.query)
            q = qs.get('q', [''])[0]
            tl = qs.get('tl', ['hi'])[0]
            if q:
                target_url = f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl={urllib.parse.quote(tl)}&q={urllib.parse.quote(q)}"
                req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
                try:
                    with urllib.request.urlopen(req) as resp:
                        audio_data = resp.read()
                        self.send_response(200)
                        self.send_header('Content-Type', 'audio/mpeg')
                        self.send_header('Content-Length', str(len(audio_data)))
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.send_header('Cache-Control', 'public, max-age=86400')
                        self.end_headers()
                        self.wfile.write(audio_data)
                        return
                except Exception as e:
                    self.send_error(500, str(e))
                    return
        super().do_GET()

    def log_message(self, format, *args):
        try:
            sys.stderr.write(f"[{self.log_date_time_string()}] {self.address_string()} {format % args}\n")
        except Exception:
            pass

def ensure_ssl_certs():
    cert_file = os.path.join(DIRECTORY, 'localhost.crt')
    key_file = os.path.join(DIRECTORY, 'localhost.key')

    if not (os.path.exists(cert_file) and os.path.exists(key_file)):
        print("[SETUP] Generating local self-signed SSL dev certificate...")
        try:
            from werkzeug.serving import make_ssl_devcert
            make_ssl_devcert(os.path.join(DIRECTORY, 'localhost'), host='localhost')
            print("[SETUP] SSL certificates generated successfully.")
        except Exception as e:
            print(f"[WARNING] Could not generate SSL certificate via werkzeug: {e}")
            print("[INFO] Please run: pip install -r requirements.txt")
            return None, None
    return cert_file, key_file

def start_https_server(cert_file, key_file):
    server_address = ('0.0.0.0', HTTPS_PORT)
    try:
        httpd = http.server.ThreadingHTTPServer(server_address, HubRequestHandler)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=cert_file, keyfile=key_file)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        print(f" [HTTPS]  https://localhost:{HTTPS_PORT}/")
        httpd.serve_forever()
    except Exception as e:
        print(f"[HTTPS ERROR] Could not start HTTPS on port {HTTPS_PORT}: {e}")

def start_http_server():
    server_address = ('0.0.0.0', HTTP_PORT)
    try:
        httpd = http.server.ThreadingHTTPServer(server_address, HubRequestHandler)
        print(f" [HTTP]   http://localhost:{HTTP_PORT}/ (Zero-SSL warnings fallback)")
        httpd.serve_forever()
    except Exception as e:
        print(f"[HTTP ERROR] Could not start HTTP on port {HTTP_PORT}: {e}")

def run():
    print("=" * 68)
    print("      PUSHTI STUDY HUB - LOCAL DEVELOPMENT SERVER")
    print("=" * 68)
    print(f"[DIRECTORY] {DIRECTORY}\n")
    print("[ACTIVE ENDPOINTS]")

    cert_file, key_file = ensure_ssl_certs()

    # Start HTTP server thread
    http_thread = threading.Thread(target=start_http_server, daemon=True)
    http_thread.start()

    # Start HTTPS server thread
    if cert_file and key_file:
        https_thread = threading.Thread(target=start_https_server, args=(cert_file, key_file), daemon=True)
        https_thread.start()
    else:
        print("[NOTICE] Running in HTTP-only mode on port 8000 due to missing SSL cert.")

    time.sleep(0.5)
    print("\n[DIRECT CHAPTER LINKS]")
    print(f"  * Paath 1 (Humko Man Ki Shakti Dena):")
    print(f"    HTTPS: https://localhost:{HTTPS_PORT}/chapters/hindi/hindi_ch1.html")
    print(f"    HTTP:  http://localhost:{HTTP_PORT}/chapters/hindi/hindi_ch1.html")
    print(f"  * Paath 2 (Rashtrasant Tukdoji):")
    print(f"    HTTPS: https://localhost:{HTTPS_PORT}/chapters/hindi/hindi_ch2.html")
    print(f"    HTTP:  http://localhost:{HTTP_PORT}/chapters/hindi/hindi_ch2.html")
    print(f"  * Paath 3 (Haar Ki Jeet):")
    print(f"    HTTPS: https://localhost:{HTTPS_PORT}/chapters/hindi/hindi_ch3.html")
    print(f"    HTTP:  http://localhost:{HTTP_PORT}/chapters/hindi/hindi_ch3.html")
    print("=" * 68)
    print("[TIP] If Chrome/Edge displays 'Your connection isn't private' on HTTPS:")
    print("      Click 'Advanced' -> 'Proceed to localhost (unsafe)' once, OR")
    print("      type 'thisisunsafe' on your keyboard, OR use the HTTP link above.")
    print("=" * 68)
    print("Server is active. Press Ctrl+C to stop.\n")
    sys.stdout.flush()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down Pushti Study Hub server.")

if __name__ == '__main__':
    run()
