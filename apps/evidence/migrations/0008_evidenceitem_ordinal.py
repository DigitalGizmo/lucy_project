# Generated by Django 4.2.3 on 2024-06-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0007_evidenceitem_transcript'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidenceitem',
            name='ordinal',
            field=models.IntegerField(default=99),
        ),
    ]
