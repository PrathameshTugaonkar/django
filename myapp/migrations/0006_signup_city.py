# Generated by Django 2.0 on 2020-04-09 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]