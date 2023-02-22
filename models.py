# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Crest(models.Model):
    crest_id = models.IntegerField(primary_key=True)
    crest_url = models.CharField(max_length=300, db_collation='latin1_swedish_ci')
    name_id = models.IntegerField()
    caption = models.CharField(max_length=255, db_collation='latin1_swedish_ci')
    clan = models.IntegerField()
    condicion = models.IntegerField()

    class Meta:
        db_table = 'crest'


class Family(models.Model):
    name_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=10000)
    clan = models.IntegerField()
    country = models.CharField(max_length=100)
    last_update = models.DateTimeField()
    has_content = models.IntegerField()
    condicion = models.IntegerField()

    class Meta:
        db_table = 'family'


class Image(models.Model):
    img_id = models.IntegerField(primary_key=True)
    image_info = models.CharField(max_length=1000, db_collation='latin1_swedish_ci')
    image_url = models.CharField(max_length=1000, db_collation='latin1_swedish_ci')
    name_id = models.IntegerField()
    type = models.CharField(max_length=255, db_collation='latin1_swedish_ci')
    condicion = models.IntegerField()

    class Meta:
        db_table = 'image'

