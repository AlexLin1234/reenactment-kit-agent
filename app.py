import os

import openai
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from reenactment_agent.runner import run_pipeline
import io
import zipfile
import requests

class PipelineRequest(BaseModel):
    century: str
    region: str
    role: str


class ZipRequest(BaseModel):
    references: dict[str, dict[str, str]]

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


def _categorize_item(name: str) -> str:
    lowered = name.lower()
    if any(k in lowered for k in ["helm", "hat", "coif", "head"]):
        return "head"
    if any(k in lowered for k in ["breast", "cuirass", "torso", "chest", "armor"]):
        return "chest"
    if any(k in lowered for k in ["leg", "chauss", "greave", "pant"]):
        return "legs"
    return "misc"

@app.post("/api/pipeline")
def pipeline(req: PipelineRequest):
    """Run the reenactment pipeline and return results."""
    return run_pipeline(req.century, req.region, req.role)


@app.post("/api/references_zip")
def references_zip(req: ZipRequest):
    """Download reference images and return a zip archive."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        for item, ref in req.references.items():
            url = ref.get("image_url")
            if not url:
                continue
            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
            except Exception:
                continue
            category = _categorize_item(item)
            ext = url.split(".")[-1].split("?")[0]
            filename = f"{category}/{item.replace(' ', '_')}.{ext}"
            zf.writestr(filename, resp.content)
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="application/zip", headers={"Content-Disposition": "attachment; filename=references.zip"})
