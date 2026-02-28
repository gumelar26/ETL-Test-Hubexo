import os
import time

from src.utils.reader import read_json
from src.utils.writer import write_json
from src.transformers.address_transformer import transform

json_file_input = "data/int_test_input/input_sample.json"
json_file_output = "data/int_test_output/output_sample.json"

data = read_json(json_file_input)
data_transformed = transform(data)

write_json(data_transformed, json_file_output)