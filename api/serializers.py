from rest_framework import serializers
from api.models import Family


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        
        model=Family
        fields=('name_id','name','info','clan','country',
		'last_update','has_content','condicion',)
