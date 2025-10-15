import socketserver


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
