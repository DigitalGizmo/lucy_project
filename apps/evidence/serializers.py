from rest_framework import serializers
from .models import EvidenceItem

class FieldQuillSerializer(serializers.Field):
    def to_representation(self, value):
        # Assuming `value` is an instance of your FieldQuill class
        return {
            'plain': value.plain,
            'html': value.html,
        }
    
    def to_internal_value(self, data):
        pass

class EvidenceItemSerializer(serializers.HyperlinkedModelSerializer):
    # relateds = serializers.IDRelatedField(many=True)
    full_text = FieldQuillSerializer()
    class Meta:
        model = EvidenceItem
        fields = [
            'slug','title', 'menu_blurb', 
            'full_text', 'item_type', 'year',
            'source', 'citation', 'accession_num'
            # 'relateds'          
        ]
        lookup_field = 'slug'