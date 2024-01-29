from django.urls import path

from .views import initial_component_fetch, csv_file_info_fetch, csv_file_data_fetch, cmp_trigger
urlpatterns=[
    path('trigger/', cmp_trigger.handle),
    path('fetch-components/',  initial_component_fetch.handle),
    path('fetch-csv-file-info/', csv_file_info_fetch.handle),
    path('file-data-page/', csv_file_data_fetch.index),
]
