# agents/supplier_recommender.py
from pydantic import BaseModel
from agents import Agent
from reenactment_agent.tools.recommend_suppliers import recommend_suppliers

class SupplierList(BaseModel):
    suppliers: list[str]
    """List of vendor or craftsman names for each gear item."""

supplier_recommender_agent = Agent(
    name="VendorFinderAgent",
    instructions=(
        "You are a vendor recommendation expert specializing in historical reenactment gear. For each item of historical equipment, recommend reputable modern vendors or craftspeople based on an internal vendor knowledge base (RAG). If no known vendor is available, perform a targeted search to find possible suppliers. Prioritize historically accurate makers praised by the reenactment community."
    ),
    tools=[recommend_suppliers],
    output_type=SupplierList,
    model="gpt-4-1106-preview"
)
