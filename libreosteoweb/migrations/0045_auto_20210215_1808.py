# Generated by Django 2.2 on 2021-02-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreosteoweb', '0044_auto_20200815_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.FileField(upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='fileimport',
            name='file_examination',
            field=models.FileField(blank=True, upload_to='tmp/'),
        ),
        migrations.AlterField(
            model_name='fileimport',
            name='file_patient',
            field=models.FileField(upload_to='tmp/'),
        ),
    ]
