# Generated by Django 3.0.3 on 2020-05-09 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20200509_1528'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='billing_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.BillingProfile'),
        ),
    ]
