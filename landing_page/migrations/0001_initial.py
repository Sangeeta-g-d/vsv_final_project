# Generated by Django 4.2.6 on 2024-02-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('contact_no', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]