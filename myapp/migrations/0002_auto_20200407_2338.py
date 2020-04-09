# Generated by Django 3.0.5 on 2020-04-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
