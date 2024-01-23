from http.server import HTTPServer, BaseHTTPRequestHandler


html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Hello world</h1>
</body>
</html>
'''


class OurHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        self.wfile.write(html.encode('utf-8'))


def run(server_class=HTTPServer, our_handler=OurHttpHandler):
    server_address = ('', 8000)
    http = server_class(server_address, our_handler)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    run(server_class=HTTPServer)