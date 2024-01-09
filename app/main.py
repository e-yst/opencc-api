from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from opencc import OpenCC

from app.core.config import settings
from app.models import OpenCCReq, OpenCCResp

HERE = Path(__file__).parent

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.is_debug)

app.mount("/ui", StaticFiles(directory=HERE / "static", html=True), name="static")


@app.get("/", include_in_schema=False)
async def redirect_to_ui():
    return RedirectResponse("/ui")


@app.get("/healthz", tags=["status"], include_in_schema=False)
async def health_check():
    return {"status": "ok"}


@app.post("/api/opencc", response_model=OpenCCResp)
async def convert_text_to_json(req: OpenCCReq):
    converter = OpenCC(req.config.value)
    return {"text": converter.convert(req.text)}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)
