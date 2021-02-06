from django.conf.urls import url
from django.urls import path

from apps.users import views

app_name = 'actions'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.Register.as_view()),
    path('register/', views.Register.as_view())
]
