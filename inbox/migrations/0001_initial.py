# Generated by Django 3.1.7 on 2022-09-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emailData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_date', models.CharField(max_length=50)),
                ('email_from', models.CharField(max_length=200)),
                ('email_to', models.CharField(max_length=200)),
                ('email_subject', models.CharField(max_length=200)),
                ('email_body', models.CharField(max_length=500)),
            ],
        ),
    ]