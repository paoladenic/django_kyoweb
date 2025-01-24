# Generated by Django 4.2.16 on 2024-12-04 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('membership_number', models.CharField(max_length=20, unique=True)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
