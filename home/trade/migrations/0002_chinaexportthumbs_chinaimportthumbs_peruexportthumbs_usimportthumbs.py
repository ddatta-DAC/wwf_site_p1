# Generated by Django 2.2 on 2019-05-31 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChinaExportThumbs',
            fields=[
                ('panjivarecordid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('thumbs', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('clear', 'Clear')], default='clear', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ChinaImportThumbs',
            fields=[
                ('panjivarecordid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('thumbs', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('clear', 'Clear')], default='clear', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PeruExportThumbs',
            fields=[
                ('panjivarecordid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('thumbs', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('clear', 'Clear')], default='clear', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='UsImportThumbs',
            fields=[
                ('panjivarecordid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('thumbs', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('clear', 'Clear')], default='clear', max_length=5)),
            ],
        ),
    ]