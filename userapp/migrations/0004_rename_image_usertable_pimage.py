# Generated by Django 5.0.1 on 2024-01-30 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_alter_usertable_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertable',
            old_name='image',
            new_name='pimage',
        ),
    ]