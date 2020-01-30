from django.urls import path
from cidades import views

app_name    =   'cidades'

urlpatterns = [
    # city detail view
    path('city/<pk>',    views.CityDetailView.as_view(),
                                    name='city-detail'),
]

