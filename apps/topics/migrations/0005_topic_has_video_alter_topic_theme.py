# Generated by Django 4.2.3 on 2024-03-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_alter_topic_prod_status_alter_topic_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='has_video',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='theme',
            field=models.IntegerField(choices=[(0, 'Select a Theme'), (1, 'Struggle for Freedom'), (2, 'A Slave Economy'), (3, 'The Variety of Enlaved Experience (draft)'), (4, 'Control and Resistance'), (5, 'Revolutionary Ideals and Liberty'), (6, 'Holding On to Humanity'), (7, 'Myths and Assumptions')], default=0),
        ),
    ]
