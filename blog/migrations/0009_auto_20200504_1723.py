# Generated by Django 3.0.5 on 2020-05-04 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200504_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-post_date']},
        ),
    ]
