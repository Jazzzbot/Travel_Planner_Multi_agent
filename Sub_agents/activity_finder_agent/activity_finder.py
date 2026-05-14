from google.adk.agents import Agent
from prompts import ACTIVITY_FINDER_PROMPT
activity_finder_agent=Agent(
    name="ActivityFinderAgent",
    model="gemini-2.5-flash",
    description="Finds activities",
    instruction=ACTIVITY_FINDER_PROMPT,
    output_key="activity_options"
)