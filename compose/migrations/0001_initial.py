# Generated by Django 3.1.7 on 2022-09-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('sub', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
            ],
        ),
    ]
