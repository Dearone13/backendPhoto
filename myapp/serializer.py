from rest_framework import serializers
from .models import User, Post, Interaction

#Lista todos los campos de cada uno de los modelos de la base de datos
#Los transforma en formato JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    image_link = serializers.FileField(max_length=1000000)

    class Meta:
        model = Post
        fields = ['post_id', 'user_id', 'image_link', 'description_photo', 'five_starts', 'four_starts', 'three_starts', 'two_starts', 'one_starts']
        
        
class InteractionSerializer(serializers.ModelSerializer):
   class Meta:
        model=Interaction
        fields='__all__'