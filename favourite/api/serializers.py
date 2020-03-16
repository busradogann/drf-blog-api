from rest_framework import serializers

from favourite.models import Favourite


class FavouriteListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

    #Favorilerde ekli olan post tekrar eklenmeye calisildiginda hata verilir.
    def validate(self, attrs):
        queryset = Favourite.objects.filter(user=attrs['user'], post=attrs['post'])
        if queryset.exists():
            raise serializers.ValidationError("Zaten favorilere eklendi.")
        return attrs


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ['content']
