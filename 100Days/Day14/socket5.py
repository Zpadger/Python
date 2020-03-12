# 使用socketserver模块创建时间服务器

from socketserver import TCPServer, StreamRequestHandler
from time import *

class EchoRequestHandler(StreamRequestHandler):

    def handle(self):
        currtime = localtime(time())
        timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
        self.wfile.write(timestr.encode('utf-8'))

server = TCPServer(('localhost',6789),EchoRequestHandler)
server.serve_forever()