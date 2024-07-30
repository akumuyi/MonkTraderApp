from dal import autocomplete
from .models import SignalService

class AssetAutocomplete(autocomplete.Select2ListView):
    def get_list(self):
        return [choice[0] for choice in SignalService.ASSET_CHOICES]