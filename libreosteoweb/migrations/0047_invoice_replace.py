# Generated by Django 2.2 on 2021-03-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreosteoweb', '0046_officesettings_cancel_invoice_credit_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='replace',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Invoice replaced'),
        ),
    ]
