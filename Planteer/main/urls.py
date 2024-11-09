from . import views
from django.urls import path


app_name="name"

urlpatterns=[

    path("contact/",views.contact_view,name="contact_view"),
    path("message/",views.Messages_view,name="Messages_view")
   
]