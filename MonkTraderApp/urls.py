from django.urls import path, include
from . import views
from MonkTraderApp.views import SignalListView, MarketListView, EducationListView, ViewReportView, ViewSignalView, ViewEducationView, subscription_management
from .autocomplete import AssetAutocomplete
from django.conf import settings
from django.views.defaults import permission_denied
from django.contrib import admin

# Set the app name for namespacing
app_name = 'MonkTraderApp'

# Define the URL patterns for the MonkTraderApp
urlpatterns = [
    # Path for admin sites
    path('admin/', admin.site.urls),

    # User authentication paths
    path("signup/", views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Homepage paths
    path("homepage1/", views.homepage1_view, name='homepage1'),
    path("homepage2/", views.homepage2_view, name='homepage2'),

    # Market report management paths
    path('create_market_report/', views.create_market_report_view, name='create_market_report'),
    path('report/edit/<int:pk>/', views.edit_market_report_view, name='edit_report'),
    path('delete_market_report/<int:report_id>/', views.delete_market_report_view, name='delete_market_report'),

    # Signal service management paths
    path('create_signal_service/', views.create_signal_service_view, name='create_signal_service'),
    path('delete_signal_service/<int:signal_id>/', views.delete_signal_service_view, name='delete_signal_service'),

    # Educational material management paths
    path('upload_educational_material/', views.upload_educational_material_view, name='upload_educational_material'),
    path('delete_educational_material/<int:material_id>/', views.delete_educational_material_view, name='delete_educational_material'),

    # ListView paths
    path('signals/', SignalListView.as_view(), name='signal_services'),
    path('reports/', MarketListView.as_view(), name='market_reports'),
    path('educations/', EducationListView.as_view(), name='educational_materials'),
    path('analysis/', ViewReportView.as_view(), name='market_analysis'),
    path('calls/', ViewSignalView.as_view(), name='trade_calls'),
    path('learning/', ViewEducationView.as_view(), name='learning_resources'),

    # Subscription Management path
    path('subscriptions/', subscription_management, name='subscription_management'),

    # Autocomplete path
    path('asset-autocomplete/', AssetAutocomplete.as_view(), name='asset-autocomplete'),
]

# handler403 = 'django.views.defaults.permission_denied'