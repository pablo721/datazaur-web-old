# Generated by Django 4.1.3 on 2022-12-27 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_account_exchanges_alter_account_friends'),
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_watchlists', to='website.account'),
        ),
    ]