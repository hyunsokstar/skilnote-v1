# Generated by Django 3.2.10 on 2022-01-16 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts2', '0006_auto_20220117_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github4',
            field=models.CharField(default='www.github.com', max_length=20),
        ),
    ]
