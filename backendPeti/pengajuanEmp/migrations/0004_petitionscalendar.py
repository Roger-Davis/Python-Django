# Generated by Django 3.2.16 on 2023-01-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengajuanEmp', '0003_petitions_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetitionsCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50, null=True)),
                ('division', models.CharField(max_length=120, null=True)),
                ('permission_type', models.CharField(max_length=24, null=True)),
                ('reason', models.TextField(null=True)),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
            ],
        ),
    ]
