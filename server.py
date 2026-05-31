#!/usr/bin/env python3
"""
Local dev server for Kairon portfolio.
Serves dist/ (or project root as fallback) on the given port.

Usage:
    python3 server.py 8081
"""

import sys
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8081

# Serve dist/ if it exists, otherwise fall back to project root
serve_dir = os.path.join(os.path.dirname(__file__), 'dist')
if not os.path.isdir(serve_dir):
    serve_dir = os.path.dirname(__file__)

os.chdir(serve_dir)

class CleanUrlHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Translate to actual file system path
        translated = super().translate_path(path)
        # If it doesn't exist and has no extension, try appending .html
        if not os.path.exists(translated) and '.' not in os.path.basename(translated):
            html_path = translated + '.html'
            if os.path.exists(html_path):
                return html_path
        return translated

print(f'Serving {serve_dir}')
print(f'→ http://localhost:{port}\n')

HTTPServer(('', port), CleanUrlHandler).serve_forever()
