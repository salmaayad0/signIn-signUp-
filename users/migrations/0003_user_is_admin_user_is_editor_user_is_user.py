# Generated by Django 4.2.4 on 2023-08-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='admin'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_editor',
            field=models.BooleanField(default=False, verbose_name='editor'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='user'),
        ),
    ]