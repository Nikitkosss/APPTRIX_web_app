# Generated by Django 3.2 on 2023-06-02 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230601_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['published']},
        ),
    ]