# Generated by Django 3.0.4 on 2020-03-14 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_about_me'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]