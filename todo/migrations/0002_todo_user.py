# Generated by Django 2.2.5 on 2019-12-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.CharField(default='hi', max_length=10),
            preserve_default=False,
        ),
    ]
