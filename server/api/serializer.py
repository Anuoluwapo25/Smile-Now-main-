from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomerUser, Doctor, Booking, Availability


class CustomerUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError({'error': 'Invalid credentials'})

        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key}


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = CustomerUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user

    def validate_email(self, value):
        if CustomerUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_username(self, value):
        if CustomerUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value
        
class DoctorLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=None, username=email, password=password)

            if user:
                try:
                    doctor = Doctor.objects.get(user=user)
                    data['user'] = user
                    data['doctor'] = doctor
                except Doctor.DoesNotExist:
                    raise serializers.ValidationError("This user is not a registered doctor.")
            else:
                raise serializers.ValidationError("Invalid email or password provided.")
        else:
            raise serializers.ValidationError("Both 'email' and 'password' must be provided.")

        return data
    

class BookingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    services = serializers.CharField(max_length=255)
    doctor = serializers.CharField(max_length=255)
    name = serializers.PrimaryKeyRelatedField(queryset=CustomerUser.objects.all()) 
    time = serializers.TimeField()
    date = serializers.DateField()
    is_completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        book = Booking.objects.create(
            name=validated_data['name'],
            services=validated_data['services'],
            doctor=validated_data['doctor'],
            time=validated_data['time'],
            date=validated_data['date'],
            is_completed=validated_data.get('is_completed', False)
        )
        return book
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.services = validated_data.get('services', instance.services)
        instance.doctor = validated_data.get('doctor', instance.dentist)
        instance.time = validated_data.get('time', instance.time)
        instance.date = validated_data.get('date', instance.date)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance


class AvailabilityCheckSerializer(serializers.Serializer):
    doctor = serializers.CharField()
    date = serializers.DateField()
    time = serializers.TimeField()

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'user', 'specialization']

class AvailabilitySerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Availability
        fields = ['id', 'doctor', 'date', 'start_time', 'end_time', 'is_available']

    def create(self, validated_data):
        doctor = self.context['request'].user.doctor_profile
        return Availability.objects.create(doctor=doctor, **validated_data)