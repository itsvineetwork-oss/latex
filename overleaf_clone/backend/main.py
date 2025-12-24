from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, JSONResponse
import tempfile
import subprocess
import os

app = FastAPI()

@app.post("/compile")
async def compile(tex_source: str = Form(...)):
    tmpdir = tempfile.mkdtemp()
    texfile = os.path.join(tmpdir, "main.tex")
    with open(texfile, "w", encoding="utf-8") as f:
        f.write(tex_source)
    cmd = [
        "pdflatex",
        "-halt-on-error",
        "-interaction=nonstopmode",
        "-output-directory",
        tmpdir,
        texfile,
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if proc.returncode != 0:
            return JSONResponse(status_code=400, content={"error": proc.stdout + "\n" + proc.stderr})
        # second run for references
        subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        pdf_path = os.path.join(tmpdir, "main.pdf")
        if not os.path.exists(pdf_path):
            return JSONResponse(status_code=500, content={"error": "PDF not generated"})
        return FileResponse(pdf_path, media_type="application/pdf", filename="main.pdf")
    except subprocess.TimeoutExpired:
        return JSONResponse(status_code=500, content={"error": "pdflatex timed out"})
