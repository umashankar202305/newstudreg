# Generated by Django 4.1.7 on 2023-05-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regapp', '0002_alter_suserreg_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suserreg',
            name='phone_no',
            field=models.IntegerField(max_length=10),
        ),
    ]
