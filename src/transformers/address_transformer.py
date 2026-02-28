import os
from dotenv import load_dotenv

from src.integrations.geocode_util import get_structured_address

load_dotenv()

def transform(address_iter):
    """
    Transforms an iterator of address dictionaries by enriching each address.
    Yields enriched addresses one by one.
    """
    token = os.getenv("LOCATIONIQ_API_KEY")

    if not token:
        raise ValueError("LOCATIONIQ_API_KEY not found in environment variables")
    
    for record in address_iter:
        structured_address = get_structured_address(
            token, 
            record['project_address']
        )

        record_enriched = record.copy()
        record_enriched['structured_address'] = structured_address
        
        yield record_enriched
