# Generated by Django 3.0.5 on 2020-05-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200504_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
