from django.urls import path
from .views import VisualizerView,export_users_xls,ContactUs, AboutUs


urlpatterns = [
    path('<int:voting_id>/', VisualizerView.as_view()),
    path('contactUs/', ContactUs.as_view()),
    path('aboutUs/', AboutUs.as_view()),
    path('<int:voting_id>/excel', export_users_xls, name='<int:voting_id>/excel'),
]
