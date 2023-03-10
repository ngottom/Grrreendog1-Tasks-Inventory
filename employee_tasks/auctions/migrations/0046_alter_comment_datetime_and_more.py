# Generated by Django 4.1.3 on 2023-01-27 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0045_timestamp_listing_alter_comment_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='2023-01-27 12:52:44', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeecomment',
            name='datetime',
            field=models.CharField(default='2023-01-27 12:52:44', max_length=100),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='datetime',
            field=models.CharField(default='12:52:44 01-27-2023', max_length=100),
        ),
        migrations.CreateModel(
            name='taskTimestamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.CharField(default='12:52:44 01-27-2023', max_length=100)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taskTimestampUser', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.employee')),
            ],
        ),
    ]
