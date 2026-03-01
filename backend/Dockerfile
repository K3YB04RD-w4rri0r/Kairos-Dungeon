FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

# Run as non-root user in production (SEC-06)
RUN adduser --disabled-password --gecos "" appuser
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/health')" || exit 1
# Also available at /healthz for Kubernetes-style probes

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
# For running tests inside Docker, add a dev stage:
#   COPY requirements-dev.txt .
#   RUN pip install -r requirements-dev.txt
#   COPY pyproject.toml .
#   COPY tests/ ./tests/
