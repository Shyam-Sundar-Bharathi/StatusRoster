# Generated by Django 5.0.3 on 2024-03-21 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StatusRosterApp', '0007_cluster_name_alter_cluster_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roster',
            name='comment',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
