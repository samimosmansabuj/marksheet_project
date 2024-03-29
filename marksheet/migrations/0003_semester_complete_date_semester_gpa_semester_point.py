# Generated by Django 5.0.1 on 2024-02-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marksheet', '0002_alter_subject_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='complete_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='semester',
            name='gpa',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='semester',
            name='point',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
    ]
