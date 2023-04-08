import http.server
import socketserver
import os
cwd = r"c:\Users\kianm\OneDrive\Documents\Programming\Python"
PORT = 8000
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_len = int(self.headers.get('content-length'))
        post_body = self.rfile.read(content_len)
        orient = 0
        if 'land' in str(post_body):
            orient = 0
            pos = 0
        elif 'port' in str(post_body):
            orient = 270
            pos = -500
        # if 'flip' in str(post_body):
        #     orient += 180
        # print(os.getcwd())
        os.system(rf'{cwd}\DisplayRotate\display64.exe /device 2 /rotate {str(orient)} /position -700 {str(pos)} > nul 2>&1')
        
        self.send_response(200)
        self.end_headers()
        return

    def log_message(self, format, *args):
        pass

Handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # print("Http Server Serving at port", PORT)
    httpd.serve_forever()