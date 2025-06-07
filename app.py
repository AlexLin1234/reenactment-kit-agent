from fastapi import FastAPI
from pydantic import BaseModel
from reenactment_agent.runner import run_pipeline

class PipelineRequest(BaseModel):
    century: str
    region: str
    role: str

app = FastAPI()

@app.post("/api/pipeline")
def pipeline(req: PipelineRequest):
    """Run the reenactment pipeline and return results."""
    return run_pipeline(req.century, req.region, req.role)
