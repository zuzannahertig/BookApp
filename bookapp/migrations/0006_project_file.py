# Generated by Django 4.1.3 on 2022-12-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0005_remove_project_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.FileField(default=1, upload_to='', verbose_name='plik'),
            preserve_default=False,
        ),
    ]