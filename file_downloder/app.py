from .services import Handler, Server


class FileDownloader(object):

    def __init__(self, port=8000):
        self.port = port

    def run(self):

        with Server(("", self.port), Handler) as httpd:
            print(f"服务启动成功, 运行端口为 {self.port}")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n服务已停止")
