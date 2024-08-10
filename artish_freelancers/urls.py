from django.urls import path
from .views import FreelancersListView, FreelancerView


urlpatterns = [
    path('', FreelancersListView.as_view()),
    path('<str:id>/', FreelancerView.as_view()),
    # path('api/auth/login/', CustomAuthToken.as_view()),
]
