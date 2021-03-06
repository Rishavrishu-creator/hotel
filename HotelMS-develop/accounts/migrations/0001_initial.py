# Generated by Django 3.0.6 on 2020-06-23 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(db_index=True, max_length=50, unique=True)),
                ('Password', models.CharField(max_length=20)),
                ('Confirmation_Status', models.BooleanField(default=False)),
            ],
        ),
    ]
