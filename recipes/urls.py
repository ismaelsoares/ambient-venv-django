from django.urls import path
from django.http import HttpResponse
from recipes.views import home_view, contact_view, about_view

# HTTP REQUEST <= HTTP RESPONSE
# HTTP REQUEST

# um array contendo os caminhos das urls e setando para as funções estabelecidas
urlpatterns = [
    path('', home_view),
    path('about/', about_view),
    path('contact/', contact_view)

]
