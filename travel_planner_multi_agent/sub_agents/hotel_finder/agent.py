from google.adk.agents import Agent
from .prompts import HOTEL_FINDER_INSTRUCTION
from ...tools import search_hotels
hotel_finder = Agent(
    name="hotel_finder",
    model="gemini-2.5-flash-lite",
    description="Searches for available hotels",
    instruction=HOTEL_FINDER_INSTRUCTION,
    # tools=[search_hotels],
    output_key="hotel_options" 
)
