from django.urls import path
from .views import VisualizerView,export_users_xls


urlpatterns = [
    path('<int:voting_id>/', VisualizerView.as_view()),
    path('<int:voting_id>/excel', export_users_xls, name='<int:voting_id>/excel'),
]
