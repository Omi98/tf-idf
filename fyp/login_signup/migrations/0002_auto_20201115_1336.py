# Generated by Django 3.0.1 on 2020-11-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='area',
            field=models.CharField(max_length=150),
        ),
    ]
