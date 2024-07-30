from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Define a custom user model extending the default Django AbstractUser
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Unique email field for the user
    membership_status = models.CharField(
        max_length=10,  # Maximum length of membership status
        choices=[('premium', 'Premium'), ('freemium', 'Freemium')],  # Choices for membership status
        null=True  # Allow null values
    )

    def __str__(self):
        return self.username  # String representation of the user

# Define a model for market reports
class MarketReport(models.Model):
    title = models.CharField(max_length=1000, default='Report Title')  # Title of the market report
    report = models.TextField(default='Enter Report')  # Content of the market report
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Author of the report
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the report was created

    class Meta:
        ordering = ['-created_at']  # Order reports by creation date, newest first

    def __str__(self):
        return self.title  # String representation of the market report

# Define a model for signal services
class SignalService(models.Model):
    # Choices for currency pairs
    CURRENCY_CHOICES = [
        ('AUDCAD', 'AUDCAD'), ('AUDCHF', 'AUDCHF'), ('AUDJPY', 'AUDJPY'),
        ('AUDNZD', 'AUDNZD'), ('AUDSGD', 'AUDSGD'), ('AUDUSD', 'AUDUSD'),
        ('CADCHF', 'CADCHF'), ('CADJPY', 'CADJPY'), ('CHFJPY', 'CHFJPY'),
        ('EURAUD', 'EURAUD'), ('EURCAD', 'EURCAD'), ('EURCHF', 'EURCHF'),
        ('EURGBP', 'EURGBP'), ('EURHKD', 'EURHKD'), ('EURHUF', 'EURHUF'),
        ('EURJPY', 'EURJPY'), ('EURNOK', 'EURNOK'), ('EURNZD', 'EURNZD'),
        ('EURSGD', 'EURSGD'), ('EURTRY', 'EURTRY'), ('EURUSD', 'EURUSD'),
        ('GBPAUD', 'GBPAUD'), ('GBPCAD', 'GBPCAD'), ('GBPCHF', 'GBPCHF'),
        ('GBPJPY', 'GBPJPY'), ('GBPNZD', 'GBPNZD'), ('GBPSGD', 'GBPSGD'),
        ('GBPUSD', 'GBPUSD'), ('MXNJPY', 'MXNJPY'), ('NOKJPY', 'NOKJPY'),
        ('NZDCAD', 'NZDCAD'), ('NZDCHF', 'NZDCHF'), ('NZDJPY', 'NZDJPY'),
        ('NZDSGD', 'NZDSGD'), ('SGDJPY', 'SGDJPY'), ('USDCAD', 'USDCAD'),
        ('USDCHF', 'USDCHF'), ('USDCNH', 'USDCNH'), ('USDDKK', 'USDDKK'),
        ('USDHUF', 'USDHUF'), ('USDJPY', 'USDJPY'), ('USDMXN', 'USDMXN'),
        ('USDNOK', 'USDNOK'), ('USDPLN', 'USDPLN'), ('USDSGD', 'USDSGD'),
        ('USDTRY', 'USDTRY'), ('USDZAR', 'USDZAR'), ('ZARJPY', 'ZARJPY'),
        ('NZDUSD', 'NZDUSD'), ('USDHKD', 'USDHKD')
    ]

    # Choices for indices and commodities
    INDICES_COMMODITIES_CHOICES = [
        ('XAGUSD', 'XAGUSD'), ('XPTUSD', 'XPTUSD'), ('XAUUSD', 'XAUUSD'),
        ('UKOUSD', 'UKOUSD'), ('USOUSD', 'USOUSD'), ('AUS200', 'AUS200'),
        ('EUSTX50', 'EUSTX50'), ('FRA40', 'FRA40'), ('GER30', 'GER30'),
        ('HK50', 'HK50'), ('SPX500', 'SPX500'), ('NDX100', 'NDX100'),
        ('NTH25', 'NTH25'), ('SWI20', 'SWI20'), ('UK100', 'UK100'),
        ('US30', 'US30')
    ]

    # Combine currency choices and indices/commodities choices
    ASSET_CHOICES = CURRENCY_CHOICES + INDICES_COMMODITIES_CHOICES

    asset = models.CharField(max_length=10, choices=ASSET_CHOICES)  # Asset type
    bias = models.CharField(max_length=4, choices=[('BUY', 'BUY'), ('SELL', 'SELL')])  # Buy or sell bias
    entry = models.DecimalField(max_digits=10, decimal_places=4)  # Entry price
    SL = models.DecimalField(max_digits=10, decimal_places=4)  # Stop loss price
    TP = models.DecimalField(max_digits=10, decimal_places=4)  # Take profit price
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the signal was created
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # User who created the signal

    def __str__(self):
        return self.asset  # String representation of the signal service

# Define a model for educational content
class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # User who uploaded the educational material
    title = models.CharField(max_length=255, default='Report Title')  # Title of the educational material
    file = models.FileField(upload_to='static/education/')  # File upload field for educational materials
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the material was created

    class Meta:
        ordering = ['-created_at']  # Order materials by creation date, newest first

    def __str__(self):
        return self.title  # String representation of the educational material

# Define a model for user subscriptions
class Subscription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # User associated with the subscription
    subscription_type = models.CharField(max_length=100)  # Type of subscription (e.g., premium, freemium)
    start_date = models.DateField(auto_now_add=True)  # Start date of the subscription
    end_date = models.DateField()  # End date of the subscription
    is_active = models.BooleanField(default=True)  # Indicates if the subscription is active

    def __str__(self):
        return f"{self.user.username} - {self.subscription_type}"  # String representation of the subscription
