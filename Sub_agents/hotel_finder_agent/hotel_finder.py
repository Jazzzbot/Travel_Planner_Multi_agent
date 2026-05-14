from google.adk.agents import Agent
from .prompts import HOTEL_FINDER_INSTRUCTIONS

hotel_finder_agent = Agent(
    name="HotelFinderAgent",
    model="gemini-2.5-flash",
    description="Searches for hotels",
    instruction= HOTEL_FINDER_INSTRUCTIONS,
    output_key= "hotel_options"
)