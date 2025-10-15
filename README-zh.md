## 文件下载服务

一个零依赖、即开即用的轻量级静态文件下载服务。基于 Python 标准库 `http.server` + 多线程 `socketserver` 实现，默认从工作目录下的
`data` 目录对外提供静态文件目录浏览与下载能力。

- **运行环境**: Python >= 3.14（推荐使用 `uv` 管理环境）
- **默认端口**: 8000
- **数据目录**: `data/`（Docker 下为容器内 `/app/data`）

---

### 特性

- **零依赖**：不依赖第三方库，拉起即用。
- **并发友好**：使用线程混入的 TCP 服务器，默认支持多请求同时下载。
- **简单易用**：将文件放入 `data/`，浏览器打开 `http://localhost:8000/` 即可下载。
- **容器支持**：提供 `Dockerfile` 与 `docker-compose.yaml`，方便本地/生产部署。

---

### 目录结构

```text
./
├─ docker/
│  └─ docker-compose.yaml   # docker-compose 文件
├─ file_downloder/
│  ├─ app.py                # 服务入口
│  └─ services/
│     ├─ server.py          # 多线程服务器
│     └─ handler.py         # 简易静态文件处理器
├─ main.py                  # 启动文件
├─ Dockerfile
├─ pyproject.toml
├─ uv.lock
└─ LICENSE
```

---

### 快速开始

#### 方式一：使用 uv（推荐）

1) 安装 `uv`（参考官方文档安装，仅需一次）：`https://github.com/astral-sh/uv`

2) 在项目根目录创建数据目录（若不存在）：

```bash
mkdir -p data
```

3) 启动服务：

```bash
uv run main.py
```

4) 打开浏览器访问：`http://localhost:8000/`

将待下载的文件放入 `data/` 目录，即可在页面中看到并下载。

#### 方式二：直接用系统 Python 运行

```bash
python3 -V         # 确认版本 >= 3.14
mkdir -p data
python3 main.py
```

#### 方式三：Docker Compose

项目已提供 `docker/docker-compose.yaml`：

```bash
cd docker
docker compose up -d
```

默认会将 `docker/volumes` 目录挂载到容器内 `/app/data`，并在主机的 `8000` 端口暴露服务。

---

### 使用说明

- **添加文件**：将文件放进 `data/`（Docker Compose 场景下为宿主机挂载目录）。
- **浏览与下载**：打开 `http://localhost:8000/` 会显示目录列表，点击文件即可下载。
- **直接链接下载**：也可直接访问 `http://localhost:8000/<文件名>`。

---

### 配置与自定义

当前默认端口为 `8000`。若需要修改端口，可在 `main.py` 中以参数形式传入：

```python
from file_downloder import FileDownloader

if __name__ == "__main__":
    FileDownloader(port=8080).run()
```

> 注意：Docker 与 Compose 场景下，可通过映射修改对外端口（如 `-p 9000:8000`），容器内仍监听 `8000`。

数据目录默认为 `data/`，若需自定义根目录，可在 `file_downloder/services/handler.py` 的处理器初始化处调整 `directory` 参数。

---

### 常见问题（FAQ）

- **访问 404/空目录**：确认 `data/` 目录存在，且已放入文件。
- **中文/特殊字符文件名**：浏览器直链下载时请确保 URL 已正确编码。
- **生产部署建议**：建议置于反向代理（如 Nginx）之后；必要时关闭目录索引（需自定义处理器逻辑），并限制对外暴露的路径。

---

### 许可证

本项目采用 `LICENSE` 中所述的许可证条款。


