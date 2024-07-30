# Generated by Django 4.2.7 on 2024-07-27 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MonkTraderApp', '0003_alter_signalservice_asset_delete_signal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketreport',
            name='user',
        ),
        migrations.AlterField(
            model_name='marketreport',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='signalservice',
            name='asset',
            field=models.CharField(choices=[('AUDCAD', 'AUDCAD'), ('AUDCHF', 'AUDCHF'), ('AUDJPY', 'AUDJPY'), ('AUDNZD', 'AUDNZD'), ('AUDSGD', 'AUDSGD'), ('AUDUSD', 'AUDUSD'), ('CADCHF', 'CADCHF'), ('CADJPY', 'CADJPY'), ('CHFJPY', 'CHFJPY'), ('EURAUD', 'EURAUD'), ('EURCAD', 'EURCAD'), ('EURCHF', 'EURCHF'), ('EURGBP', 'EURGBP'), ('EURHKD', 'EURHKD'), ('EURHUF', 'EURHUF'), ('EURJPY', 'EURJPY'), ('EURNOK', 'EURNOK'), ('EURNZD', 'EURNZD'), ('EURSGD', 'EURSGD'), ('EURTRY', 'EURTRY'), ('EURUSD', 'EURUSD'), ('GBPAUD', 'GBPAUD'), ('GBPCAD', 'GBPCAD'), ('GBPCHF', 'GBPCHF'), ('GBPJPY', 'GBPJPY'), ('GBPNZD', 'GBPNZD'), ('GBPSGD', 'GBPSGD'), ('GBPUSD', 'GBPUSD'), ('MXNJPY', 'MXNJPY'), ('NOKJPY', 'NOKJPY'), ('NZDCAD', 'NZDCAD'), ('NZDCHF', 'NZDCHF'), ('NZDJPY', 'NZDJPY'), ('NZDSGD', 'NZDSGD'), ('SGDJPY', 'SGDJPY'), ('USDCAD', 'USDCAD'), ('USDCHF', 'USDCHF'), ('USDCNH', 'USDCNH'), ('USDDKK', 'USDDKK'), ('USDHUF', 'USDHUF'), ('USDJPY', 'USDJPY'), ('USDMXN', 'USDMXN'), ('USDNOK', 'USDNOK'), ('USDPLN', 'USDPLN'), ('USDSGD', 'USDSGD'), ('USDTRY', 'USDTRY'), ('USDZAR', 'USDZAR'), ('ZARJPY', 'ZARJPY'), ('NZDUSD', 'NZDUSD'), ('USDHKD', 'USDHKD'), ('XAGUSD', 'XAGUSD'), ('XPTUSD', 'XPTUSD'), ('XAUUSD', 'XAUUSD'), ('UKOUSD', 'UKOUSD'), ('USOUSD', 'USOUSD'), ('AUS200', 'AUS200'), ('EUSTX50', 'EUSTX50'), ('FRA40', 'FRA40'), ('GER30', 'GER30'), ('HK50', 'HK50'), ('SPX500', 'SPX500'), ('NDX100', 'NDX100'), ('NTH25', 'NTH25'), ('SWI20', 'SWI20'), ('UK100', 'UK100'), ('US30', 'US30')], max_length=7),
        ),
        migrations.AlterField(
            model_name='signalservice',
            name='bias',
            field=models.CharField(max_length=4),
        ),
    ]
