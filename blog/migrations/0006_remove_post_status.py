# Generated by Django 4.2.8 on 2024-02-06 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comment_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
