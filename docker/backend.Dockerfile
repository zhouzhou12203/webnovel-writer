ARG PYTHON_BASE=python:3.11-slim
FROM ${PYTHON_BASE}

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 分层缓存：先复制依赖声明
COPY backend/requirements.txt /app/backend/requirements.txt
COPY .claude/scripts/requirements.txt /app/.claude/scripts/requirements.txt

RUN pip install --no-cache-dir -r /app/backend/requirements.txt \
    && pip install --no-cache-dir -r /app/.claude/scripts/requirements.txt

# 复制源码
COPY backend /app/backend
COPY .claude /app/.claude

EXPOSE 8080
WORKDIR /app/backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
