FROM python:3.11-slim

# Install TeX Live (kept reasonably scoped)
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-xetex \
    latexmk \
    build-essential \
    poppler-utils \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY backend /app
COPY frontend /app/frontend

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
