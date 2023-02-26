# Generated by Django 4.1.7 on 2023-02-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crest',
            fields=[
                ('crest_id', models.IntegerField(primary_key=True, serialize=False)),
                ('crest_url', models.CharField(db_collation='latin1_swedish_ci', max_length=300)),
                ('name_id', models.IntegerField()),
                ('caption', models.CharField(db_collation='latin1_swedish_ci', max_length=255)),
                ('clan', models.IntegerField()),
                ('condicion', models.IntegerField()),
            ],
            options={
                'db_table': 'crest',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('name_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=10000)),
                ('clan', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField()),
                ('has_content', models.IntegerField()),
                ('condicion', models.IntegerField()),
            ],
            options={
                'db_table': 'family',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('img_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image_info', models.CharField(db_collation='latin1_swedish_ci', max_length=1000)),
                ('image_url', models.CharField(db_collation='latin1_swedish_ci', max_length=1000)),
                ('name_id', models.IntegerField()),
                ('type', models.CharField(db_collation='latin1_swedish_ci', max_length=255)),
                ('condicion', models.IntegerField()),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
