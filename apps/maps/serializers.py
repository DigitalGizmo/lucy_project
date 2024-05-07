from rest_framework import serializers
from .models import Map, Related

class RelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Related
        fields = ['title', 'content_type', 'slug', 'link']

class FieldQuillSerializer(serializers.Field):
    def to_representation(self, value):
        # Assuming `value` is an instance of your FieldQuill class
        return {
            'plain': value.plain,
            'html': value.html,
        }
    
    def to_internal_value(self, data):
        pass

class MapSerializer(serializers.HyperlinkedModelSerializer):
    relateds = RelatedSerializer(many=True, read_only=True)
    full_text = FieldQuillSerializer()
    class Meta:
        model = Map
        fields = [
            'slug','title', 'menu_blurb', 
            'full_text', 'relateds', 'prod_status'
        ]
        lookup_field = 'slug'