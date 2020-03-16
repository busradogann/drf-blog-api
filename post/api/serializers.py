from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):  # serializers'in seralizer'i kullanilirsa field'lar tek tek tanimlanmak zorunda(model'deki field'larla ayni olmali)

    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )

    # # # api'de Foreignkey'li user field'ini id yerine ismiyle goruntulemek icin birinci yontem.
    # username = serializers.SerializerMethodField(method_name="username_new")

    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'username',
            'title',
            'content',
            'media',
            'slug',
            'created',
            'modified_by',
            'url',
        ]

    # # api'de Foreignkey'li user field'ini id yerine ismiyle goruntulemek icin birinci yontem.
    # def username_new(self, obj):
    #     return str(obj.user.username)

    def get_username(self, obj):
        return str(obj.user.username)


class PostUpdateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'media',
        ]

    #update() methodu override ediliyor.
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.media = validated_data.get('media', instance.media)
    #     instance.save()
    #     return instance

    #validasyon islemleri
    def validate(self, attrs):
        if attrs['title'] == 'title':
            raise serializers.ValidationError("boyle title mi olur")
        if attrs['content'] == 'content':
            raise serializers.ValidationError("boyle content olmaz")
        return attrs

