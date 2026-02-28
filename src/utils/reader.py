import json

def read_json(path: str) -> dict:
    """
    Reads JSON files from a specified directory and yields each record.
    Args:
        path (str): The directory containing JSON files.
    Yields:
        dict: Each record from the JSON files.
    """
    
    with open(path, "r") as file:
        data = json.load(file)
        
        if not isinstance(data, list):
            raise ValueError("Json must contain list of record")

        for record in data:
            yield record
