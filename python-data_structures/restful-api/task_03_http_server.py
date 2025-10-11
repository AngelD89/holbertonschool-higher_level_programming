#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import json

HOST = "127.0.0.1"
PORT = 8000

class SimpleAPIHandler(BaseHTTPRequestHandler):
    # --- helpers -------------------------------------------------------------
    def write_text(self, status: int, text: str):
        data = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def write_json(self, status: int, obj: dict):
        data = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    # --- routing -------------------------------------------------------------
    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":  # root
            return self.write_text(200, "Hello, this is a simple API!")

        elif path == "/status":
            # spec says this should return "OK"
            return self.write_text(200, "OK")

        elif path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            return self.write_json(200, payload)

        elif path == "/info":
            payload = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            return self.write_json(200, payload)

        # anything else -> 404 JSON error
        return self.write_json(404, {"error": "Endpoint not found"})

    # Optional: small POST example (handy for testing with curl)
    def do_POST(self):
        path = urlparse(self.path).path
        content_length = int(self.headers.get("Content-Length", "0") or 0)
        body = self.rfile.read(content_length) if content_length > 0 else b""

        if path == "/echo":
            try:
                parsed = json.loads(body.decode("utf-8") or "{}")
            except json.JSONDecodeError:
                return self.write_json(400, {"error": "Invalid JSON"})
            return self.write_json(201, {"received": parsed})

        return self.write_json(404, {"error": "Endpoint not found"})

    # make server logs a little cleaner (optional)
    def log_message(self, fmt, *args):
        return  # comment this out if you want default request logs

def run():
    server = ThreadingHTTPServer((HOST, PORT), SimpleAPIHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("\nServer stopped.")

if __name__ == "__main__":
    run()
