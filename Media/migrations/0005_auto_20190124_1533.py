# Generated by Django 2.1.4 on 2019-01-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0004_auto_20190124_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='video_src',
            field=models.CharField(default='', max_length=100),
        ),
    ]