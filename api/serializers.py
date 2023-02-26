from rest_framework import serializers
from api.models import Family, Crest, Image

class ImageSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Image
        fields = ('img_id', 'image_url')

class CrestSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Crest
        fields = ("crest_id", "name_id")

class FamilySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    crests = CrestSerializer(many=True, read_only=True)

    class Meta:
        
        model=Family
        fields=('name_id','name','info','clan','country',
		'last_update','has_content','condicion', 'images', 'crests')

