# Generated by Django 2.1 on 2018-09-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgt', '0002_emp_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='id',
        ),
        migrations.AddField(
            model_name='emp',
            name='eid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
