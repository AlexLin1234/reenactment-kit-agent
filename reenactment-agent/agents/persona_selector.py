from pydantic import BaseModel
from openai import Agent
from tools.suggest_persona import suggest_persona

class PersonaSuggestion(BaseModel):
    persona: str
    """Suggested reenactment persona."""

persona_selector_agent = Agent(
    name="PersonaSelectorAgent",
    instructions=(
        "You are a historical consultant helping users choose a reenactment persona based on their interests in "
        "time period, region, and military role. Ask clarifying questions to narrow down the ideal historical identity."
    ),
    tools=[suggest_persona],
    output_type=PersonaSuggestion,
    model="gpt-4-1106-preview"
)
