# Generated by Django 3.0.7 on 2021-09-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='contributors',
            field=models.IntegerField(default=0),
        ),
    ]
