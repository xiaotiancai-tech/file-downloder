import http.server
import threading


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="data", **kwargs)

    def log_message(self, format, *args):
        thread_name = threading.current_thread().name
        print(f"[{thread_name}] {format % args}")
