# Generated by Django 2.1 on 2018-11-17 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181117_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.Book'),
        ),
    ]
