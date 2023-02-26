# Generated by Django 4.1.7 on 2023-02-26 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crest',
            name='name_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.family'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.family'),
        ),
    ]