from django.apps import AppConfig

class MonktraderappConfig(AppConfig):
    """
    Configuration class for the MonkTraderApp Django application.
    This class is used to configure the application and its settings.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Default field type for auto-generated primary keys
    name = 'MonkTraderApp'  # Name of the application
