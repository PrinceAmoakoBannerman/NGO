# Generated by Django 5.2.4 on 2025-07-31 22:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_mobile_number_volunteer_phone_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='donor',
        ),
        migrations.AddField(
            model_name='donation',
            name='email',
            field=models.EmailField(default='princebannerman17@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='reference',
            field=models.CharField(default='princebannerman17@gmail.com', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
