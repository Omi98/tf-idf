# Generated by Django 3.1.3 on 2020-11-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tf_idf', '0003_recommendationmodel_paper_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendationmodel',
            name='tfidf',
            field=models.DecimalField(decimal_places=15, max_digits=15),
        ),
    ]