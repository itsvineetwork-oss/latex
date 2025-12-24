Overleaf Clone - Minimal

This is a minimal Overleaf-like demo that compiles LaTeX to PDF using `pdflatex` inside a Docker container with TeX Live.

Quick start (requires Docker and docker-compose):

1. Build and run with docker-compose:

```bash
cd "d:/My-Learning/Latex Code/overleaf_clone"
docker-compose up --build
```

2. Open http://localhost:8000/frontend/index.html in your browser.
3. Edit the LaTeX in the editor and click "Compile". The compiled PDF will appear on the right.

Notes:
- The Docker image installs a subset of TeX Live. For full TeX Live, edit the Dockerfile to include `texlive-full`.
- The backend is `backend/main.py` (FastAPI) with a `/compile` endpoint.
