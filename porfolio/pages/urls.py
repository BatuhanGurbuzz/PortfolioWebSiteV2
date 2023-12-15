from django.urls import path
from .views import IndexViews, portfolio_list

urlpatterns = [
    path('', IndexViews.as_view(), name="index"),
    path('projects/', portfolio_list, name="page_projects"),  # URL'yi 'page_projects' olarak güncelledik
    path('projects/<int:project_id>/', portfolio_list, name="portfolio_detail"),
]