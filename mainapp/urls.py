from django.urls import path

from .views import initial_component_fetch, csv_file_info_fetch, csv_file_data_fetch
urlpatterns=[

    path('', initial_component_fetch.index),
    path('fetch-components/',  initial_component_fetch.handle),
    path('backend-url/', csv_file_info_fetch.index),
    path('fetch-csv-file/', csv_file_info_fetch.handle),
    path('file-data-page/', csv_file_data_fetch.index)

]
