from google.adk.agents import ParallelAgent, SequentialAgent, Agent
from Travel-Planner-Multi-agent.Sub-agents import (activity_finder_agent, flight_finder_agent, hotel_finder_agent)


parallel_search = ParallelAgent(
    name= "ParallelSearch",
    sub_agents=[
        activity_finder, flight_finder, hotel_finder
    ],
    description=" Searches for flights, hotels, activities, etc"
)

travel_plan=Agent(
    name= "travel_plan_builder",
    model = "gemini-2.5-flash",
    description="Combines all search results into one complete travel plan",
    instruction=""" 
    You are a travel planner. Create a complete, well-organized itinerary by 
    combining the search results below.

    **Available Flights:**
    {flight_options}

    **Available Hotels:**
    {hotel_options}

    **Recommended Activities:**
    {activity_options}

    Create a formatted itinerary that:
    1. Recommends the BEST option from each category (flights, hotel)
    2. Organizes activities into a day-by-day plan
    3. Includes estimated total cost
    4. Adds helpful travel tips

    Format beautifully with clear sections and markdown.
    """,
    output_key= "final_itenarary"
)

travel_plan_sequential=SequentialAgent(
    name="travel_plan_seq",
    description="Does the complete planning",
    sub_agents= [
        parallel_search,
        travel_plan
    ],
)
root_agent = travel_plan_sequential