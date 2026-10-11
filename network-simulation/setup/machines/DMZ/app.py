#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Extended to manage user keys and secrets via HTTP endpoints.

import json
import math
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

allow = True
port = 80



class RequestHandler(BaseHTTPRequestHandler):


    def send_json_response(self, status_code: int, data: dict):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")

        if allow:
            self.send_header('ACCESS-CONTROL-ALLOW-CREDENTIALS', 'true')
            self.send_header('ACCESS-CONTROL-ALLOW-HEADERS', 'Content-Type, X-ALLOWED-1, X-ALLOWED-2')
            self.send_header('ACCESS-CONTROL-ALLOW-METHODS', 'OPTIONS, GET, POST')
            self.send_header('ACCESS-CONTROL-ALLOW-ORIGIN', '*')

        self.end_headers()
        self.wfile.write(bytes(json.dumps(data, indent=2), 'utf-8'))

    def parse_request_body(self):
        content_length = self.headers.get('Content-Length')
        length = int(content_length) if content_length else 0
        if length > 0:
            raw_data = self.rfile.read(length).decode('utf-8')
            try:
                return json.loads(raw_data)
            except json.JSONDecodeError:
                return {}
        return {}

    def serve_get(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)

    
        self.send_json_response(200, {"status": "ok", "from" : "Web"})
        return

    def serve_options(self):
        self.send_json_response(200, {"status": "CORS preflight standard response"})

    do_GET = serve_get


def main():
    print(f"Listening on 0.0.0.0:{port} - {'ALLOWS' if allow else 'DISALLOWS'} CORS")
    server = HTTPServer(('0.0.0.0', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
