# Generated by Django 5.0.7 on 2024-07-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('accel_sec', models.FloatField()),
                ('top_speed_kmh', models.FloatField()),
                ('range_km', models.FloatField()),
                ('efficiency_whkm', models.FloatField()),
                ('fast_charge_kmh', models.FloatField()),
                ('rapid_charge', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('powertrain', models.CharField(max_length=255)),
                ('plug_type', models.CharField(max_length=255)),
                ('body_style', models.CharField(max_length=255)),
                ('segment', models.CharField(max_length=255)),
                ('seats', models.IntegerField()),
                ('price_euro', models.FloatField()),
            ],
        ),
    ]