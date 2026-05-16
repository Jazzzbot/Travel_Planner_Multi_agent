from google.adk.agents import Agent
from .prompts import FLIGHT_FINDER_INSTRUCTION
from ...tools import search_flights

flight_finder = Agent(
    name="flight_finder",
    model="gemini-2.5-flash-lite",
    description="Searches for available flights",
    instruction=FLIGHT_FINDER_INSTRUCTION,
    # tools=[search_flights],
    output_key="flight_options"
)
