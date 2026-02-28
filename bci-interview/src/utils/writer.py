import json
from pathlib import Path

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

if __name__ == "__main__":
    json_file_path = Path(__file__).resolve().parent.parent.parent / "data" / "int_test_output" / "output_sample.json"

    data = [
        {
            "publication_media": "Neue Zürcher Zeitung",
            "project_title": "Neubau eines Spielplatzes mit barrierefreiem Zugang und moderner Beleuchtung",
            "date_scraped": "15/03/2024 14:23:45",
            "project_address": "Bahnhofquai 8"
        },
        {
            "publication_media": "Tages-Anzeiger",
            "project_title": "Sanierung der Fassade und Installation von Solarpanels",
            "date_scraped": "22/04/2024 09:11:32",
            "project_address": "Via San Gottardo 39"
        }
    ]

    write_json(data, json_file_path)
