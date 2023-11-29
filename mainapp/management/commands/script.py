from django.core.management.base import BaseCommand
# from .csv_to_json import csv_to_json
from collections import defaultdict
import pandas as pd
import json
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        def csv_to_json(csv_file: str) -> str:
            data_dict = defaultdict(list)
            # defaultdict contaning list as default values

            df = pd.read_csv(csv_file)
            df_unique = df.drop_duplicates()
            df_unique.to_csv(csv_file, index=False)

            # re format datain csv into a "dataframe" like dict
            with open(csv_file, mode='r') as csv_file:
                csv_data = csv.DictReader(csv_file)
                for row in csv_data:  # type(row) is dict
                    for key, val in row.items():
                        data_dict[key].append(val)

            result_dict = dict(data_dict)

            # convert and return json string
            return json.dumps(result_dict, indent=4)
        self.stdout.write(csv_to_json("C:\\Users\\2003s\\OneDrive\\Desktop\\Internship\\New folder\\2_26_06_2023.csv"))
