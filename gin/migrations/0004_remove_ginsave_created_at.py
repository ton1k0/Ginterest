# Generated by Django 4.1.5 on 2023-03-12 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gin', '0003_ginsave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ginsave',
            name='created_at',
        ),
    ]
