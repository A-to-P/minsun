# Generated by Django 4.2 on 2023-06-22 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author',
        ),
    ]
