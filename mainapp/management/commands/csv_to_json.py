import csv
import json
from collections import defaultdict
# import pandas as pd

def csv_to_json(csv_file: str) -> str:
    data_dict = defaultdict(list)
        #defaultdict contaning list as default values

    with open(csv_file, mode='r') as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data: # type(row) is dict
            for key, val in row.items():
                data_dict[key].append(val)

    result_dict = dict(data_dict)

    # convert and return json string
    return json.dumps(result_dict, indent=4)
