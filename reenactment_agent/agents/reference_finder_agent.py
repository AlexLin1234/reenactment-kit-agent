# agents/reference_finder.py
from pydantic import BaseModel
from agents import Agent
from reenactment_agent.tools.fetch_references import fetch_references

class ReferenceData(BaseModel):
    image_url: str
    museum: str
    """Reference link and museum or source for the item."""

reference_finder_agent = Agent(
    name="ReferenceFinderAgent",
    instructions=(
        "You are a historical source researcher. For each piece of historical gear, you find either museum images of the actual item, surviving examples, or depictions in period artwork. Cite only reputable sources such as museum collections, illustrated manuscripts, or scholarly catalogues."
    ),
    tools=[fetch_references],
    output_type=ReferenceData,
    model="gpt-4-1106-preview"
)
