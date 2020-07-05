from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random",views.ran,name="ran"),
    path("search",views.search, name="search"),
    path("Edit:"+"<str:name>",views.edit, name="edit"),
    path("New",views.new, name="new"),
    path("error:"+"<str:error>",views.error, name="error"),
    path("<str:name>", views.page, name="page")
]
