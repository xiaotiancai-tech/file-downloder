# file-downloader

[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-GNU-green.svg)](LICENSE)

A zero-dependency, ready-to-use lightweight static file download service. Built on Python standard library
`http.server` + multi-threaded `socketserver`, it provides static file directory browsing and download capabilities from
the `data` directory under the working directory by default.

- **Runtime Environment**: Python >= 3.14 (recommended to use `uv` for environment management)
- **Default Port**: 8000
- **Data Directory**: `data/` (in Docker, it's `/app/data` inside the container)

---

## Features

- **Zero Dependencies**: No third-party libraries required, ready to use out of the box.
- **Concurrency Friendly**: Uses thread-mixed TCP server, supports multiple simultaneous download requests by default.
- **Simple to Use**: Put files in `data/`, open browser at `http://localhost:8000/` to download.
- **Container Support**: Provides `Dockerfile` and `docker-compose.yaml` for easy local/production deployment.

---

## Directory Structure

```text
./
├─ docker/
│  └─ docker-compose.yaml   # docker-compose file
├─ file_downloder/
│  ├─ app.py                # service entry point
│  └─ services/
│     ├─ server.py          # multi-threaded server
│     └─ handler.py         # simple static file handler
├─ main.py                  # startup file
├─ Dockerfile
├─ pyproject.toml
├─ uv.lock
└─ LICENSE
```

---

## Quick Start

### Method 1: Using uv (Recommended)

1) Install `uv` (refer to official documentation for installation, only needed once): `https://github.com/astral-sh/uv`

2) Create data directory in project root (if it doesn't exist):

```bash
mkdir -p data
```

3) Start the service:

```bash
uv run main.py
```

4) Open browser and visit: `http://localhost:8000/`

Put files to be downloaded into the `data/` directory, and you can see and download them from the page.

### Method 2: Run directly with system Python

```bash
python3 -V         # confirm version >= 3.14
mkdir -p data
python3 main.py
```

### Method 3: Docker Compose

The project provides `docker/docker-compose.yaml`:

```bash
cd docker
docker compose up -d
```

By default, it mounts the `docker/volumes` directory to `/app/data` inside the container and exposes the service on port
`8000` of the host.

---

## Usage Instructions

- **Adding Files**: Put files into `data/` (in Docker Compose scenario, use the host mount directory).
- **Browse and Download**: Open `http://localhost:8000/` to display directory listing, click files to download.
- **Direct Link Download**: You can also directly access `http://localhost:8000/<filename>`.

---

## Configuration and Customization

The current default port is `8000`. To modify the port, pass it as a parameter in `main.py`:

```python
from file_downloder import FileDownloader

if __name__ == "__main__":
    FileDownloader(port=8080).run()
```

> Note: In Docker and Compose scenarios, you can modify the external port through mapping (e.g., `-p 9000:8000`), while
> the container still listens on port `8000`.

The data directory defaults to `data/`. To customize the root directory, adjust the `directory` parameter in the handler
initialization in `file_downloder/services/handler.py`.

---

## FAQ

- **404/Empty Directory Access**: Confirm that the `data/` directory exists and contains files.
- **Chinese/Special Character Filenames**: When downloading via browser direct links, ensure the URL is properly
  encoded.
- **Production Deployment Recommendations**: Recommend placing behind a reverse proxy (like Nginx); disable directory
  indexing when necessary (requires custom handler logic), and limit externally exposed paths.

---

## License

This project is licensed under the terms described in `LICENSE`.

