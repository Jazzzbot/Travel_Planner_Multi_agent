from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from .sub_agents.activity_finder import activity_finder
from .sub_agents.flight_finder import flight_finder
from .sub_agents.hotel_finder import hotel_finder
from .sub_agents.weather_finder import weather_finder



parallel_search = ParallelAgent(
    name="ParallelSearch",
    sub_agents=[
        flight_finder,
        hotel_finder,
        activity_finder,
        weather_finder
        
    ],  
    description="Searches flights, hotels, weather and activities concurrently"
)


itinerary_builder = Agent(
    name="itinerary_builder",
    model="gemini-2.5-flash-lite",
    description="Combines all search results into a complete travel itinerary",
    instruction="""
    You are a travel planner. Create a complete, well-organized itinerary by 
    combining the search results below.

    **Available Flights:**
    {flight_options}

    **Available Hotels:**
    {hotel_options}

    **Weather Information:**
    {weather_info}

    **Recommended Activities:**
    {activity_options}

    Create a formatted itinerary that:
    1. Recommends the BEST option from each category (flights, hotel)
    2. Organizes activities into a day-by-day plan
    3. Factors in the weather when scheduling outdoor activities
    4. Includes a packing list based on the weather
    5. Includes estimated total cost
    6. Adds helpful travel tips

    Format beautifully with clear sections and markdown.

    """,
    output_key="final_itinerary"
)



root_agent = SequentialAgent(
    name="TravelPlanningSystem",
    sub_agents=[
        parallel_search,
        itinerary_builder
    ],
    description="Complete travel planning system with parallel search and itinerary building"
)

