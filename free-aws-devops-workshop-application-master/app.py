import http.server
import socketserver
import os

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Environment variable to append to the message, with a default
        hello_world_text = os.getenv('HELLO_WORLD_TEXT', 'default text')

        # HTML content to be served
        html_content = f"""
        <html>
        <head><title>Sample App</title></head>
        <body>
        <h1 style="font-size:80px; !important">Hello, <span style="color: orange;"> {hello_world_text}</span></h1>
        </body>
        </html>
        """.encode('utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content)

PORT = 8000

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
