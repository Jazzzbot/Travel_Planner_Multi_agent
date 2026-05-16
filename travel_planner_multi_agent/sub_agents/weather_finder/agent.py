from google.adk.agents import Agent
from .prompts import WEATHER_FINDER_INSTRUCTION
from ...tools import get_weather
weather_finder = Agent(
    name="weather_finder",
    model="gemini-2.5-flash-lite",
    description="Finds current weather and forecasts for travel destinations",
    instruction= WEATHER_FINDER_INSTRUCTION,
    # tools=[get_weather],
    output_key="weather_info"
)