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
        # Keep it simple for tests: plain text only
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def write_json(self, status: int, obj):
        data = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        # Tests expect application/json (no charset)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    # --- routing -------------------------------------------------------------
    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            return self.write_text(200, "Hello, this is a simple API!")

        if path == "/status":
            return self.write_text(200, "OK")

        if path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            return self.write_json(200, payload)

        if path == "/info":
            payload = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            return self.write_json(200, payload)

        # For undefined endpoints, tests expect *plain text* exactly:
        # "Endpoint not found"
        return self.write_text(404, "Endpoint not found")

    # Silence default logging (optional)
    def log_message(self, fmt, *args):
        return


def run():
    server = ThreadingHTTPServer((HOST, PORT), SimpleAPIHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run()
