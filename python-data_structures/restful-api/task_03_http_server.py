#!/usr/bin/env python3
"""
Simple API server using python's http.server module
Shows Basic HTTP request handling and JSON responses
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Since we are inheriting fron BaseHTTPRequestHandler -
    Class will handle different simple API endpoints
    """

    def do_GET(self):
        """
        Method will be called whenever we GET a request to our server
        """

        if self.path == '/':
            self._handle_root()
        elif self.path == '/data':
            self._handle_data()
        elif self.path == '/status':
            self._handle_status()
        else:
            self._handle_not_found()

    def _handle_root(self):
        """
        Handles requests to the root endpoint '/'
        Welcome users to the API.
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(b"Hello, this is a simple API!")

    def _handle_data(self):
        """
        Handles request to /data endpoint
        Returns JSON data about a person
        """

        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }

        json_data = json.dumps(data)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json_data.encode())

    def _handle_status(self):
        """
        Handles requests to /status endpoint
        Returns simple status information
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(b"OK")

    def _handle_not_found(self):
        """
        Handles undefined request endpoints
        Returns 404 NOT FOUND error
        """
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(b"Endpoint not found")

    def log_message(self, format, *args):
        """
        Override default logging making it more informative
        Shows requests are being made
        """
        print(f"[{self.address_string()}]{format % args}")


def run_server(port=8000):
    """
    Create and run the HTTP Server
    Sets up and begins listening for connections inbound

    Args:
        port (int): port to run server on (default:8000)
    """
    server_address = ('', port)

    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}...")

    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
