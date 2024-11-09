from . import views
from django.urls import path



app_name="plants"

urlpatterns=[
    path("",views.home_view,name="home_view"),
    path("all/plants/",views.all_plants_view,name="all_plants_view"),
    path("add/",views.add_plant,name="add_plant"),
    path("detail/<plant_id>/",views.post_detail,name="post_detail"),
    path("update/<plant_id>/",views.post_update,name="post_update"),
    path("delete/<plant_id>/",views.post_delete,name="post_delete"),
    path("search/",views.search_view,name="search_view")
]