from django.urls import path
from . import views
urlpatterns = [
    path("",views.predict_insurance,name="predict_insurance"),
]
