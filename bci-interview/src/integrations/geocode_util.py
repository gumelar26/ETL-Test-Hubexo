import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_structured_address(token: str, partial_address: str) -> list[dict]:
    """
    Given a partial address, returns the full structured address using LocationIQ API.
    Args:
        token (str): Token key that used for call locationiq API.
        partial_address (str): The partial address.
    Return:
        list[dict]: Enriched address data.
    """
    
    url = "https://us1.locationiq.com/v1/search"
    params = {
        "key" : token,
        "q": partial_address,
        "format": "json",
        "limit": 5
    }
    
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, list):
        raise ValueError(f"Unexpected response: {data}")

    return data

if __name__ == "__main__":
    token = os.getenv("LOCATIONIQ_API_KEY")

    if not token:
        raise ValueError("LOCATIONIQ_API_KEY not found in environment variables")

    address = "Bahnhofquai 8"
    result = get_structured_address(token, address) 

    print(result)  
