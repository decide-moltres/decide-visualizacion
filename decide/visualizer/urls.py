from django.urls import path,include
from .views import VisualizerView,export_users_xls,ContactUs, AboutUs
from django.conf.urls import url

urlpatterns = [
    path('<int:voting_id>/', VisualizerView.as_view()),
    path('contactUs/', ContactUs.as_view()),
    path('aboutUs/', AboutUs.as_view()),
    path('<int:voting_id>/excel', export_users_xls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
