# Generated by Django 2.0.7 on 2018-08-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180807_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='org_id',
            field=models.CharField(blank=True, default='', max_length=36, verbose_name='Organization'),
        ),
    ]
