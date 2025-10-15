import http.server
import socketserver
import threading


class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="data", **kwargs)

    def log_message(self, format, *args):
        thread_name = threading.current_thread().name
        print(f"[{thread_name}] {format % args}")


if __name__ == "__main__":
    PORT = 8000
    with ThreadedHTTPServer(("", PORT), CustomHandler) as httpd:
        print(f"服务启动成功, 运行端口为 {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务已停止")
