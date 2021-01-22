from rest_framework import serializers
from api.models import CustomUser, Prescription, Condition


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username", 
            "email", 
            "password", 
            "phone",
            "first_name", 
            "last_name"
        ]
        extra_kwargs= {"password": {'write_only': True}} #prevents the user password from being returned

    def create(self, validated_data):
        # overide create method to hash user password 
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = "__all__"