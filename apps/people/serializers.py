from rest_framework import serializers
from .models import Person, Related


class RelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Related
        fields = ['title', 'content_type', 'slug', 'link']
        # person = serializers.ReadOnlyField(source='person.slug')

class FieldQuillSerializer(serializers.Field):
    def to_representation(self, value):
        # Assuming `value` is an instance of your FieldQuill class
        return {
            # 'json_string': value.json_string,
            # 'delta': value.delta,
            'plain': value.plain,
            'html': value.html,
        }
    
    def to_internal_value(self, data):
        pass

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    relateds = RelatedSerializer(many=True, read_only=True)
    
    bio = FieldQuillSerializer()
    more_text = FieldQuillSerializer()
    class Meta:
        model = Person
        fields = [
            'slug','first_name', 'last_name', 'gender', 'enslavement_status',
            'birth_year', 'birth_month', 'birth_day', 'birth_text',
            'death_year', 'death_month', 'death_day', 'death_text',
            'menu_blurb', 'bio', 'more_text', 'has_more',
            'prod_status', 'relateds'          
        ]
        lookup_field = 'slug'