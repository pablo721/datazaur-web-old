# Generated by Django 4.1.3 on 2022-12-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
        ('website', '0002_alter_account_exchanges_alter_account_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='exchanges',
            field=models.ManyToManyField(blank=True, to='crypto.cryptoexchange'),
        ),
        migrations.AlterField(
            model_name='account',
            name='friends',
            field=models.ManyToManyField(blank=True, to='website.account'),
        ),
    ]
