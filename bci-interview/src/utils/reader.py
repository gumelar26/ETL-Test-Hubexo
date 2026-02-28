import json
from pathlib import Path

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
        for record in data:
            yield record

if __name__ == "__main__":
    json_file_path = Path(__file__).resolve().parent.parent.parent / "data" / "int_test_input" / "input_sample.json"
    
    for record in read_json(json_file_path):
        print(record)