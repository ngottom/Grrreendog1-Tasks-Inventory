# Generated by Django 4.1.3 on 2023-02-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0058_alter_comment_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='02-03-2023 13:54:12', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeecomment',
            name='datetime',
            field=models.CharField(default='02-03-2023 13:54:12', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeelisting',
            name='datetime',
            field=models.CharField(default='13:54:12 EST, 02-03-2023', max_length=100),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='datetime',
            field=models.CharField(default='13:54:12 02-03-2023', max_length=100),
        ),
    ]