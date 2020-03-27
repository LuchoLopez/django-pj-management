from rest_framework import serializers
from technologies.models import Technologie
from persons.models import PersonTech, Person


class PersonTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTech
        fiels = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    techs = serializers.SerializerMethodField('get_techs')

    def get_techs(self, obj):
        return PersonTechSerializer(obj.persontech_set.all(), many=True).data

    class Meta:
        model = Person
        fields = ['name', 'techs']
        depth = 1


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologie
        fields = '__all__'


class PersonTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTech
        fields = '__all__'


class TechCustomSerializer(serializers.Serializer):
    tech = TechSerializer()
    persons = PersonTechSerializer(many=True)
