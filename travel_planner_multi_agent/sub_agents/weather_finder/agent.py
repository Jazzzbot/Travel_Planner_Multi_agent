from google.adk.agents import Agent
from .prompts import WEATHER_FINDER_INSTRUCTION
weather_finder = Agent(
    name="weather_finder",
    model="gemini-2.5-flash",
    description="Finds current weather and forecasts for travel destinations",
    instruction= WEATHER_FINDER_INSTRUCTION,
    output_key="weather_info"
)