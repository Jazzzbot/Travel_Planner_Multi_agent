import time
import requests



# Retry helper for LLM / API rate-limit spikes
def call_with_retry(fn, *args, retries=3, wait=5, **kwargs):
    """
    Calls fn(*args, **kwargs) up to `retries` times.
    Waits `wait` seconds between attempts.
    Returns the result or a safe error dict on final failure.
    """
    for attempt in range(retries):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            error_str = str(e).lower()
            # Rate-limit / overload errors are worth retrying
            if any(k in error_str for k in ["429", "quota", "rate", "spike", "overload", "resource exhausted"]):
                if attempt < retries - 1:
                    time.sleep(wait * (attempt + 1))  # exponential back-off
                    continue
            # Any other error on last attempt → safe fallback
            return {"error": f"{fn.__name__} failed: {str(e)}"}
    return {"error": f"{fn.__name__} failed after {retries} retries"}

def get_weather(city: str, forecast_days: int = 7) -> dict:
    
    def _fetch():
        # Real API call later
        return {
            "city": city,
            "forecast": f"Simulated {forecast_days}-day forecast for {city}. Expect mild temperatures between 15-25°C with occasional rain."
        }
    
    return call_with_retry(_fetch)

def search_flights(origin: str, destination: str, departure_date: str, adults: int = 1, max_results: int = 5) -> dict:
    
    def _fetch():
        return {
            "origin": origin,
            "destination": destination,
            "flights": f"Simulated flight options from {origin} to {destination} on {departure_date}."
        }
    
    return call_with_retry(_fetch)


def search_hotels(city_code: str, check_in_date: str, check_out_date: str, adults: int = 1, max_results: int = 5) -> dict:
    
    def _fetch():
        return {
            "city": city_code,
            "hotels": f"Simulated hotel options in {city_code} from {check_in_date} to {check_out_date}."
        }
    
    return call_with_retry(_fetch)