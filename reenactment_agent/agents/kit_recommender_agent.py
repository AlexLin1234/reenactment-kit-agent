from pydantic import BaseModel
from openai import Agent
from reenactment_agent.tools.generate_kit import generate_kit_list

class KitList(BaseModel):
    items: list[str]
    """List of kit components for this persona."""

kit_recommender_agent = Agent(
    name="KitRecommenderAgent",
    instructions=(
        "You are a historical equipment specialist. Given a historical persona, generate a complete list of historically accurate gear that would have been worn or used by that person in military service."
    ),
    tools=[generate_kit_list],
    output_type=KitList,
    model="gpt-4-1106-preview"
)
