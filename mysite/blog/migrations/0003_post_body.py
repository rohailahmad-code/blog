# Generated by Django 3.1.1 on 2020-10-16 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
