# Generated by Django 4.2.5 on 2023-10-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_announcements_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
