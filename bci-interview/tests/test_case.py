import json
from pathlib import Path

from src.utils.reader import read_json
from src.transformers.address_transformer import transform

BASE_DIR = Path(__file__).resolve().parent.parent
json_path = BASE_DIR / "data" / "int_test_input" / "input_sample.json"
input_sample = [
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

class TestCase:
    def test_file_contain_list(self):
        data = list(read_json(json_path))
        assert isinstance(data, list)
    
    def test_read_json_success(self):
        result = list(read_json(json_path))
        assert result == input_sample

    def test_transform_success(self):
        sample_geocode_respose = [
            {
                "place_id": "72066280",
                "licence": "https://locationiq.com/attribution",
                "osm_type": "way",
                "osm_id": "1062629834",
                "boundingbox": ["47.3776855", "47.3777968", "8.5416158", "8.5416197"],
                "lat": "47.3777388",
                "lon": "8.5416197",
                "display_name": "Bahnhofquai, City, Altstadt, Zurich, District Zurich, Zurich, 8001, Switzerland",
                "class": "highway",
                "type": "tertiary",
                "importance": 0.2634118478675517
            },
            {
                "place_id": "72144767",
                "licence": "https://locationiq.com/attribution",
                "osm_type": "way",
                "osm_id": "294148769",
                "boundingbox": ["47.3782843", "47.3785179", "8.5413708", "8.5414564"],
                "lat": "47.3784122",
                "lon": "8.5413887",
                "display_name": "Bahnhofquai, City, Altstadt, Zurich, District Zurich, Zurich, 8021, Switzerland",
                "class": "highway",
                "type": "tertiary",
                "importance": 0.2634118478675517
            },
            {
                "place_id": "72181945",
                "licence": "https://locationiq.com/attribution",
                "osm_type": "way",
                "osm_id": "1411243431",
                "boundingbox": ["47.3754211", "47.3756972", "8.5418926", "8.5419368"],
                "lat": "47.3756972",
                "lon": "8.5419368",
                "display_name": "Bahnhofquai, Lindenhof, Altstadt, Zurich, District Zurich, Zurich, 8001, Switzerland",
                "class": "highway",
                "type": "tertiary",
                "importance": 0.2634118478675517
            },
            {
                "place_id": "72262299",
                "licence": "https://locationiq.com/attribution",
                "osm_type": "way",
                "osm_id": "8139899",
                "boundingbox": ["47.3783115", "47.3785059", "8.5417017", "8.5418224"],
                "lat": "47.3784253",
                "lon": "8.5417239",
                "display_name": "Bahnhofquai, City, Altstadt, Zurich, District Zurich, Zurich, 8092, Switzerland",
                "class": "highway",
                "type": "tertiary",
                "importance": 0.2634118478675517
            },
            {
                "place_id": "72187151",
                "licence": "https://locationiq.com/attribution",
                "osm_type": "way",
                "osm_id": "4950245",
                "boundingbox": ["47.3760075", "47.3769173", "8.5414806", "8.541738"],
                "lat": "47.3761727",
                "lon": "8.5416967",
                "display_name": "Bahnhofquai, Lindenhof, Altstadt, Zurich, District Zurich, Zurich, 8001, Switzerland",
                "class": "highway",
                "type": "residential",
                "importance": 0.2634118478675517
            }
        ]

        result = list(transform(input_sample))

        assert result[0]["structured_address"] == sample_geocode_respose
        assert result[0]["project_address"] == "Bahnhofquai 8"
    



    



