# Generated by Django 3.1.2 on 2020-10-16 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developerverse', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]