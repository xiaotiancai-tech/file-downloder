FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

COPY . .

RUN uv sync
RUN mkdir data

EXPOSE 8000

CMD ["uv", "run", "main.py"]
