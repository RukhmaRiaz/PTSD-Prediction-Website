# Generated by Django 3.0.14 on 2023-01-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_doctor_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=20)),
                ('rpassword', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
