# Generated by Django 2.1.7 on 2019-02-27 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20190226_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='editors',
            field=models.ManyToManyField(blank='True', related_name='editors', to='lists.User'),
        ),
        migrations.AlterField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(blank='True', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='lists.User'),
        ),
    ]