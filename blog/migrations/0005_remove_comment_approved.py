# Generated by Django 4.2.8 on 2024-02-05 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
    ]