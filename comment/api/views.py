from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import DestroyModelMixin

from comment.api.paginations import CommentPagination
from favourite.api.paginations import FavouritePagination
from comment.api.permissions import IsOwner
from comment.api.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer
from comment.models import Comment


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)#request'in user'i giris yapmissa comment olusturulur.


class CommentListAPIView(ListAPIView):
    # queryset = Comment.objects.all() get_queryset methodu eklemdigi icin queryset kaldirildi.
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination

    #queryset degiskeni kaldirilip get_queryset methodu kullanildi. Burada queryset filtrelenebiliyor parent'i olmayanlara gore.
    def get_queryset(self):
        queryset = Comment.objects.filter(parent=None) #parent'i olmayan comment'ler cekildi.
        query = self.request.GET.get("q") #get request'in query value'su yakalandi.
        if query: #query true ise
            queryset = queryset.filter(post=query) #queryset query'ye gore filtrelendi.
        return queryset


class CommentUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    serializer_class = CommentDeleteUpdateSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwner] #yorumun sahibi giris yapmissa yorumu sadece o guncelleyebilir.
    lookup_field = 'pk' #update islemi lookup_field'da belirtilen field'a gore yapilir.

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#CommentUpdateAPIView'in icinde DestroyModelMixin ile delete islemi yapildigi icin CommentDeleteAPIView class'i kaldirirldi.

# class CommentDeleteAPIView(DestroyAPIView): #UpdateModelMixin, RetrieveModelMixin
#     serializer_class = CommentDeleteUpdateSerializer
#     queryset = Comment.objects.all()
#     permission_classes = [IsOwner] #yorumun sahibi giris yapmissa yorumu sadece o silebilir.
#     lookup_field = 'pk' #delete islemi lookup_field'da belirtilen field'a gore yapilir.

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
