from django.core.management.base import BaseCommand
from mainapp.models import CsvFileInfo as Cfi, CsvFileData as Cfd, Component as Comp
from django.db import IntegrityError
from .csv_to_json import csv_to_json
from .check_for_output import check_for_output
from .cycles import cycles
from datetime import datetime
import time
import os
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        OUTPUT_FOLDER = "C:\\Users\\2003s\\OneDrive\\Desktop\\Internship\\Output"
        INPUT_FOLDER = "C:\\Users\\2003s\\OneDrive\\Desktop\\Internship\\New Folder"

        while True:
            if (check_for_output(OUTPUT_FOLDER)):
                output_file = os.path.join(OUTPUT_FOLDER, "output.txt")

                with open(output_file) as file:
                    x_dist = file.readline().strip()
                    max_def = file.readline().strip()
                    angle = file.readline().strip()
                    csv_file = os.path.join(INPUT_FOLDER, file.readline().strip())
                    c_time = datetime.fromtimestamp(os.path.getctime(csv_file))
                    self.stdout.write("csv_file_info fetched")
                os.remove(output_file)

                # Push the fetched data to DB

                cfi_rec= Cfi(# this record pushed into CsvFileInfo
                        creation_time= c_time,
                        x_distance= x_dist,
                        servo_angle= angle,
                        max_deflection= max_def,
                        component_serial_num= Comp.objects.latest("component_serial_num"),
                        cycles= cycles(csv_file)
                    )
                cfi_rec.save()
                # call csv_to_json which returns a dict
                insert_json= json.loads(csv_to_json(csv_file))
                Cfd(
                    csv_file_serial_num= cfi_rec,
                    bend_data= insert_json
                ).save()

                os.remove(os.path.join(INPUT_FOLDER, csv_file))

            time.sleep(0.5)

