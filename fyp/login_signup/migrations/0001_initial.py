# Generated by Django 3.0.1 on 2020-11-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.IntegerField()),
                ('paper_title', models.CharField(max_length=200)),
                ('author_keywords', models.CharField(max_length=200)),
                ('abstract', models.CharField(max_length=2000)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
    ]
