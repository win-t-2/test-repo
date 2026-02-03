#!/usr/bin/env python3
"""
Simple HTTP server that serves "hello world" text.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys


class HelloWorldHandler(BaseHTTPRequestHandler):
    """HTTP request handler that returns 'hello world' for all requests."""

    def do_GET(self):
        """Handle GET requests."""
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'hello world')

    def log_message(self, format, *args):
        """Log server messages to stdout."""
        print(f"{self.address_string()} - {format % args}")


def run_server(host='0.0.0.0', port=8000):
    """Start the HTTP server."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, HelloWorldHandler)
    print(f'Starting HTTP server on {host}:{port}...')
    print(f'Server running at http://{host}:{port}/')
    print('Press Ctrl+C to stop the server')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down server...')
        httpd.shutdown()
        sys.exit(0)


if __name__ == '__main__':
    # Default port is 8000, but can be overridden via command line argument
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f'Error: Invalid port number "{sys.argv[1]}"')
            sys.exit(1)

    run_server(port=port)
