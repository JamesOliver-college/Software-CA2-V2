# Generated by Django 2.2.7 on 2019-12-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='headline',
            field=models.CharField(default='headline', max_length=200),
        ),
    ]
