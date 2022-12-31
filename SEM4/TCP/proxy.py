import socketserver
import http.server
import urllib
import requests


class MyProxyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]
        response = requests.get(url)
        return urllib.request.urlopen(response.url)

        
proxyObject = MyProxyRequestHandler
proxyServer = socketserver.TCPServer(('localhost', 8000), proxyObject)
proxyServer.serve_forever()
