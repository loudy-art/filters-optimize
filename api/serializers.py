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

class FamilySerializerHistory(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    crests = CrestSerializer(many=True, read_only=True)

    class Meta:
        
        model=Family
        fields=('name_id','name','clan','country', 'info',
                'last_update','has_content','condicion', 'images', 'crests')
    

class FamilySerializerProductsCrest(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    crests = CrestSerializer(many=True, read_only=True)

    class Meta:
        
        model=Family
        fields=('name_id','name','clan','country',
                'last_update','has_content','condicion', 'images', 'crests')


class FamilySerializerCrest(serializers.ModelSerializer):
    crests = CrestSerializer(many=True, read_only=True)
    class Meta:
        
        model=Family
        fields=('name_id','name','clan','country',
                'last_update','has_content','condicion', 'crests')
        

class FamilySerializerProducts(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        
        model=Family
        fields=('name_id','name','clan','country',
                'last_update','has_content','condicion', 'images')

class FamilySerializerHistoryCrest(serializers.ModelSerializer):
    crests = CrestSerializer(many=True, read_only=True)

    class Meta:
        
        model=Family
        fields=('name_id','name','clan','country',
                'last_update','has_content','condicion', 'info', 'crest')

class FamilySerializerGeneral(serializers.ModelSerializer):
    class Meta:
        
        model=Family
        fields=('name_id','name','clan','country',
                'last_update','has_content','condicion')
        

class FamilySerializerHistoryProd(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        
        model=Family
        fields=('name_id','name','clan','country',
                'last_update','has_content','condicion', 'info', 'images')
