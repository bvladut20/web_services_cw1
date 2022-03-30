from django.contrib.auth.models import User, Group
from rest_framework import serializers
from teaching.models import Professor, Module, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'code', 'name', 'overall_rating', 'number_ratings']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'code', 'name', 'professors', 'semester', 'year']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'value', 'professor', 'module']

    # create new rating and update professor's overall rating
    def create(self, validated_data):
        professor_data = validated_data.get("professor")
        rating_value = validated_data.get("value")

        if professor_data.overall_rating is None:
            professor_data.overall_rating = 0.0

        professor_data.number_ratings += 1
        professor_data.total_ratings_sum = professor_data.total_ratings_sum + rating_value
        professor_data.overall_rating = professor_data.total_ratings_sum / professor_data.number_ratings
        professor_data.overall_rating = round(professor_data.overall_rating, 2)
        professor_data.save()

        return Rating.objects.create(**validated_data)

