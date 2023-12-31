# Generated by Django 3.1.6 on 2021-10-23 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0005_auto_20211022_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='contributors',
        ),
        migrations.AddField(
            model_name='media',
            name='deleted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('stripe_receipt', models.CharField(max_length=2000)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.campaign')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
