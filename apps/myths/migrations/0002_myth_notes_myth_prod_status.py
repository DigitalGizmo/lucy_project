# Generated by Django 4.2.3 on 2023-12-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myth',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='myth',
            name='prod_status',
            field=models.IntegerField(choices=[(0, 'hide'), (1, 'show'), (2, 'active')], default=1),
        ),
    ]
