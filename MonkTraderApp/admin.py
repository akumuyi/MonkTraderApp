from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SignalService, MarketReport, Education, Subscription
from .forms import SignalServiceForm

# Register models here 
admin.site.register(CustomUser, UserAdmin)

# Register SignalServiceForm
class SignalServiceAdmin(admin.ModelAdmin):
    form = SignalServiceForm

# Register SignalService, MarketReport, Education models and Subscription
admin.site.register(SignalService, SignalServiceAdmin)
admin.site.register(MarketReport)
admin.site.register(Education)
admin.site.register(Subscription)