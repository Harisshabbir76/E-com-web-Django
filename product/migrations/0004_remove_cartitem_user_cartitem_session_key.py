# Generated by Django 5.1.3 on 2024-12-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='session_key',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]