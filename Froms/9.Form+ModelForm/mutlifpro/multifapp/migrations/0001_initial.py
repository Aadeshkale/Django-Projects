# Generated by Django 2.1 on 2018-10-16 06:27

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'reg',
            },
            managers=[
                ('obj', django.db.models.manager.Manager()),
            ],
        ),
    ]
