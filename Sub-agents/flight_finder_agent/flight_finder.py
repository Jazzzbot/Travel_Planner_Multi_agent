from google.adk.agents import Agent
from prompts import FLIGHT_FINDER_PROMPTS
flight_finder_agent=Agent(
    name="FlightFinderAgent",
    model="gemini-2.5-flash",
    description="Searches for flights",
    instruction= FLIGHT_FINDER_PROMPTS,
    output_key="flight_options"
)