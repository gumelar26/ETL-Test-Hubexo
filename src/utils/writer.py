import json

def write_json(data, path: str) -> None:
    """
    Writes an iterator of dicts to a JSON file.
    Args:
        data (iterable): An iterator of dictionaries to write to the JSON file.
        path (str): The file path where the JSON data will be written.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write("[\n")

        first = True
        for item in data:
            if not first:
                f.write(",\n")
            json.dump(item, f, ensure_ascii=False)
            first = False

        f.write("\n]")
