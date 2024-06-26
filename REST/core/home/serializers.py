from rest_framework import serializers
from .models import Person
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = ['name','age']
        # fields = ['name']         # name is required
        fields = '__all__'      # all fields
        # exclude = ['name']  # name feild will be excluded
    
    # Validation
    def validate_age(self, age):
        print(age)
        return age

    def validate (self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('age should be grater than 18')

        return data
