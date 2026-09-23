from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "service": "aws-ai-ops-app",
                "hostname": socket.gethostname()
            }

            body = json.dumps(response).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        else:
            body = b"AWS AI Ops Platform"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def log_message(self, format, *args):
        print(format % args)

server = HTTPServer(("0.0.0.0", 8080), Handler)
print("AWS AI Ops application listening on port 8080")
server.serve_forever()
