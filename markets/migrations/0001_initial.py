# Generated by Django 4.1 on 2022-09-03 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=32)),
                ('last', models.FloatField()),
                ('last_close', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('change', models.FloatField()),
                ('change_percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('symbol', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('asset_class', models.CharField(choices=[(0, 'cryptocurrency'), (1, 'currency'), (2, 'commodity'), (3, 'equity'), (4, 'bond'), (5, 'real estate'), (6, 'fund share'), (7, 'na')], default='na', max_length=16)),
                ('group', models.CharField(blank=True, choices=[(0, 'metals'), (1, 'softs'), (2, 'meats'), (3, 'energy'), (4, 'grains'), (5, 'na')], max_length=21, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('symbol', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('asset_class', models.CharField(choices=[(0, 'cryptocurrency'), (1, 'currency'), (2, 'commodity'), (3, 'equity'), (4, 'bond'), (5, 'real estate'), (6, 'fund share'), (7, 'na')], default='na', max_length=16)),
                ('issuer_id', models.CharField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('code', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('mic', models.CharField(max_length=64)),
                ('timezone', models.CharField(max_length=64)),
                ('hours', models.CharField(max_length=64)),
                ('country_code', models.CharField(max_length=8)),
                ('source', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('name', models.CharField(max_length=64)),
                ('symbol', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('country_id', models.CharField(max_length=2)),
                ('currency_code', models.CharField(max_length=3)),
                ('index_type', models.CharField(default='na', max_length=32)),
                ('value', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.CharField(max_length=32)),
                ('quote', models.CharField(max_length=32)),
                ('bid', models.FloatField(blank=True, null=True)),
                ('ask', models.FloatField(blank=True, null=True)),
                ('source', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_id', models.CharField(blank=True, max_length=3, null=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('displaySymbol', models.CharField(blank=True, max_length=16, null=True)),
                ('figi', models.CharField(blank=True, max_length=12, null=True)),
                ('isin', models.CharField(blank=True, max_length=12, null=True)),
                ('mic', models.CharField(blank=True, max_length=16, null=True)),
                ('shareClassFIGI', models.CharField(blank=True, max_length=16, null=True)),
                ('symbol', models.CharField(blank=True, max_length=16, null=True)),
                ('symbol2', models.CharField(blank=True, max_length=16, null=True)),
                ('stock_class', models.CharField(blank=True, max_length=32, null=True)),
                ('type', models.CharField(max_length=32)),
                ('exchange', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='markets.exchange')),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=16)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('exchange', models.CharField(blank=True, max_length=64, null=True)),
                ('type', models.CharField(max_length=32)),
                ('exchangeShortName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='security_exchange', to='markets.exchange')),
            ],
        ),
    ]
