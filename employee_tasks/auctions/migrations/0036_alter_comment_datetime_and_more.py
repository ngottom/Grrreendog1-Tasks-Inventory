# Generated by Django 4.1.3 on 2023-01-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_alter_comment_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='2023-01-19 10:21:32', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeecomment',
            name='datetime',
            field=models.CharField(default='2023-01-19 10:21:32', max_length=100),
        ),
    ]
