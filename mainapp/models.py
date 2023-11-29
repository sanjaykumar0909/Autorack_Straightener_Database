from django.db import models

class Component(models.Model):
    component_serial_num = models.AutoField(primary_key= True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

class CsvFileInfo(models.Model):
    csv_file_serial_num = models.AutoField(primary_key= True)
    component_serial_num = models.ForeignKey(
        Component,
        null= True,
        on_delete= models.CASCADE,
        to_field= "component_serial_num",
        related_name= "component_serial_num_fk"
    )
    creation_time = models.DateTimeField(null= True)
    cycles = models.IntegerField(null=True)
    x_distance = models.FloatField(null= True)
    servo_angle = models.FloatField(null= True)
    max_deflection = models.FloatField(null= True)

class CsvFileData(models.Model):
    csv_file_serial_num = models.OneToOneField(
        CsvFileInfo,
        on_delete= models.CASCADE,
        primary_key= True,
        to_field= "csv_file_serial_num"
    )
    bend_data = models.JSONField(null=True)
