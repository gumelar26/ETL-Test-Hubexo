import requests

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
        "limit": 3
    }
    
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, list):
        raise ValueError(f"Unexpected response: {data}")

    return data

