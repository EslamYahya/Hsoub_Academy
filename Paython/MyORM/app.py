from datetime import datetime
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from Model import Model
from Field import *
from DataBase import Database

Model.db = Database('database.sqlite')
Model.connection = Model.db.connect()

PORT = 8000

class Post(Model):
    tittle = CharField
    body = TextField
    created_at = DataTimeField()
    published = BooleanFeild()


class User(Model):
    first_name = CharField
    last_name = CharField(max_length=255)
    age = IntegerField()



if __name__ == '__main__':

    class MyHandler(SimpleHTTPRequestHandler):
        def do_Get(self):
            if self.path == '/':
                return SimpleHTTPRequestHandler.do_GET(self)

            elif self.path == '/posts':
                 self.send_response(200)
                 self.send_header('Content-type', 'application/json')
                 self.end_headers()
                 self.wfile.write(json.dumps(Post.all()).encode('utf-8'))
            else:
                Post_id = int(self.path.split('/')[-1])
                result = Post.get(Post_id)
                if result is False:
                    self.send_response(404)
                    self.wfile.write(b'Not Found')
                    return
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end.headers()
                self.wfile.write(json.dumps(Post.get(Post_id)).encode('utf-8'))

        def do_POST(self):
            length = int(self.headers.get('content-length'))
            body = self.rfile.read(length)
            string = urlparse(body)
            post = parse_qs(string.path.decode('utf-length'))
            post.create(title=post['title'][0], body=post[0], created_at=datetime.now(), published=False)
            self.send_response(301)
            self.send_header('Location', 'localhost:8000')
            self.end_headers()

    with HTTPServer(("", PORT), MyHandler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()

