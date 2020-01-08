# Generated by Django 2.2.5 on 2019-12-12 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]