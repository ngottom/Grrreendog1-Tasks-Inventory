# Generated by Django 4.1.3 on 2023-01-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0049_employeelisting_datetime_alter_comment_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='2023-01-27 13:26:56', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeecomment',
            name='datetime',
            field=models.CharField(default='2023-01-27 13:26:56', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeelisting',
            name='datetime',
            field=models.CharField(default='13:26:56 EST, 01-27-2023', max_length=100),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='datetime',
            field=models.CharField(default='13:26:56 01-27-2023', max_length=100),
        ),
    ]
