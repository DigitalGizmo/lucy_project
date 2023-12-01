from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
            'first_name', 'last_name', 'gender', 'enslavement_status',
            'birth_year', 'birth_month', 'birth_day',
            'death_year', 'death_month', 'death_day',
            'menu_blurb', 'prod_status'            
        ]