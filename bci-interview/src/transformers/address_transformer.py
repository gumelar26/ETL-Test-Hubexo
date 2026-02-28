from dotenv import load_dotenv
import os

load_dotenv()

def transform(address_iter):
    """
    Transforms an iterator of address dictionaries by enriching each address.
    Yields enriched addresses one by one.
    """
    token = os.getenv("LOCATIONIQ_API_KEY")

    if not token:
        raise ValueError("LOCATIONIQ_API_KEY not found in environment variables")
    
    enrich_address = get_structured_address(token, address_iter)
    
    yield enrich_adress
