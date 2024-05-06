# Generated by Django 4.2.3 on 2024-05-06 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_topic_caption_topic_has_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='related',
            name='content_type',
            field=models.CharField(choices=[('select', 'please select'), ('evidence', 'evidence'), ('maps', 'maps'), ('people', 'people'), ('topics', 'topics')], default='select', max_length=12),
        ),
        migrations.AddField(
            model_name='related',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='related',
            name='link',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
