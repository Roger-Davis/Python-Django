# Generated by Django 3.2.16 on 2023-02-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20230106_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteshrd',
            name='type_notes',
            field=models.TextField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='noteshrd',
            name='notes',
            field=models.TextField(max_length=230, null=True),
        ),
    ]
