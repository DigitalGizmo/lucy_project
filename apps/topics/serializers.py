from rest_framework import serializers
from .models import Topic, Related

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

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    relateds = RelatedSerializer(many=True, read_only=True)
    full_text = FieldQuillSerializer()
    class Meta:
        model = Topic
        fields = [
            'slug','title', 'menu_blurb', 'theme', 'has_video', 'has_image',
            'full_text', 'caption', 'relateds', 'prod_status'
        ]
        lookup_field = 'slug'