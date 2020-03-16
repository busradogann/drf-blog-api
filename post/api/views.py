from rest_framework.generics import (
                                ListAPIView,
                                RetrieveAPIView,
                                RetrieveUpdateAPIView,
                                DestroyAPIView,
                                CreateAPIView,
)
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework.filters import SearchFilter, OrderingFilter

from post.api.paginations import PostPagination
from post.api.permissions import IsOwner
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer
from post.models import Post


class PostListAPIView(ListAPIView, CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #pagination yapar.
    pagination_class = PostPagination

    #title'a ve content'e gore filtreleme yapar.
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['title', 'content']

    #taslakta olan postlari ceker(draft=True).
    # def get_queryset(self):
    #     queryset = Post.objects.filter(draft=True)
    #     return queryset

    #post() handler methoduyla CreateModelMixin'in icindeki create methodu cagrilarak listAPIView'e post request yapma ozelligi kazandirildi.
    def post(self, request, *args, **kwargs):
        print(self.request.__dict__)
        return self.create(request, *args, **kwargs)

    #perform_create() methoduyla sadece o request'i atan kullanicinin post yapmasi saglandi.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView): #herkes retrieve yapabilir.
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug' #lookup_field'da verilen field'a gore detay sayfasina gider.


#PostUpdateAPIView'a Destroy ozelligi getirildigi icin PostDeleteAPIView class'i kaldirildi.
# class PostDeleteAPIView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsOwner] #custom permission
#     lookup_field = 'slug' #lookup_field'da verilen field'a gore o sayfayi siler.


class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    permission_classes = [IsOwner, IsAdminUser]
    lookup_field = 'slug' #lookup_field'da verilen field'a gore o sayfayi update eder.

    def perform_update(self, serializer):
        print(type(self))
        print(self.__dict__)
        print(type(self.request))
        print(self.request.__dict__)
        print(self.request.user)
        serializer.save(modified_by=self.request.user)#update eden kisi kimse onu kaydeder.

    #DestroyModelMixin'i icindeki destroy methodu ile PostUpdateAPIView'ina delete request ozelligi kazandirildi.
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostCreateAPIView(CreateAPIView, ListModelMixin): #sadece giris yapmis kullanicinin create yetkisi vardir.
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    #ListModelMixin'in icindeki list() methodu kullanilarak Create sayfasinda listeleme saglandi.
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

