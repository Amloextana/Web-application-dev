# Generated by Django 4.2.5 on 2023-09-15 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CubeSat', '0006_alter_employer_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CubeSat.customer'),
        ),
    ]
