from rest_framework import serializers
from .models import ResumeDesciption,Resume

class ResumeDesciptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResumeDesciption
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resume
        fields = '__all__'