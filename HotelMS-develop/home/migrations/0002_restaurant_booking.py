# Generated by Django 3.0.6 on 2020-06-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant_Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('Number_of_persons', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
