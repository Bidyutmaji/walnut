from rest_framework import serializers

class AgeSerializer(serializers.Serializer):
    day = serializers.IntegerField()
    month = serializers.IntegerField()
    year = serializers.IntegerField()
    