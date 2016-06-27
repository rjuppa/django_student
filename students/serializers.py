from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, School, Classroom


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


# Serializers define the API representation.
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('classroom', 'user', 'comment', 'created')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name',)


class ClassroomSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ('id', 'name', 'school', 'students')






