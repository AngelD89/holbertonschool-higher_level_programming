#!/usr/bin/env python3
"""
A tiny API built with Python's built-in http.server.

Endpoints:
  GET  /         -> "Hello, this is a simple API!"
  GET  /status   -> "OK"
  GET  /data     -> JSON: {"name": "John", "age": 30, "city": "New York"}
  GET  /info     -> JSON: {"version": "1.0", "description": "A simple API built with http.server"}
  POST /echo     -> Echoes JSON you send (bonus: demonstrates POST handling)

Any other path -> 404 with JSON error.
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import json

HOST = "127.0.0.1"
PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    # ---------- helpers ----------
    def _write_bytes(self, status: int, body: bytes, content_type: str):
        self.send_response(status)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def write_text(self, status: int, text: str):
        self._write_bytes(status, text.encode("utf-8"), "text/plain")

    def write_json(self, status: int, obj):
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self._write_bytes(status, data, "application/json")

    # ---------- routing ----------
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

        # Unknown route
        return self.write_json(404, {"error": "Endpoint not found"})

    def do_POST(self):
        """Bonus: demonstrate POST handling with a simple JSON echo endpoint."""
        path = urlparse(self.path).path

        # Read request body (if any)
        content_length = int(self.headers.get("Content-Length", "0") or 0)
        raw = self.rfile.read(content_length) if content_length > 0 else b""

        if path == "/echo":
            # Expect JSON, return it back
            try:
                data = json.loads(raw.decode("utf-8") or "{}")
            except json.JSONDecodeError:
                return self.write_json(400, {"error": "Invalid JSON"})
            return self.write_json(201, {"received": data})

        return self.write_json(404, {"error": "Endpoint not found"})

    # Make logs quieter (optional)
    def log_message(self, fmt, *args):
        return  # comment this line if you want default logging


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
