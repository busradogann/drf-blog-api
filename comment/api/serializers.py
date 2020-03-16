from django.contrib.auth.models import User
from rest_framework import serializers

from comment.models import Comment
from post.models import Post


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created']

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].post != attrs['parent']:
                raise serializers.ValidationError("something went wrong")
        return attrs


class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer): #user modeli icin serializer olusturuldu, istenmeyen field'lari cikarmak icin.
    #Yoksa CommentListSrializer'da depth=1 deyip user modeli getirilebiliyordu.
    class Meta:
        model = User
        exclude = ['password']


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'id']


class CommentListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = UserSerializer()
    username = serializers.SerializerMethodField(method_name="get_username")
    post = PostCommentSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
        # depth = 1 #api'de sadece id'si gorunen user ve post field'larinin iclerindeki fieldlar gosterildi(ic ice serializer).
        #depth, tum field'lari gosterir, istenmeyen field varsa ayrica serializer yazmak lazim(bakiniz; UserSerializer).

    #ic ice yorumlari gosterme
    def get_replies(self, obj): #serializer objesi aliyor
        if obj.any_children: #Serializer objesinin any_children'i True ise
            return CommentChildSerializer(obj.children(), many=True).data #objenin children'ini serilestirecek.

    def get_username(self, obj):
        return str(obj.user.username)


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]
