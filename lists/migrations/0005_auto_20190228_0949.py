# Generated by Django 2.1.7 on 2019-02-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20190227_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='edits',
            field=models.ManyToManyField(related_name='edits', to='lists.List'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='owns',
            field=models.ManyToManyField(related_name='owns', to='lists.List'),
        ),
    ]
