from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from favourite.api.paginations import FavouritePagination
from favourite.api.permissions import IsOwner
from favourite.api.serializers import FavouriteListCreateSerializer, FavouriteSerializer
from favourite.models import Favourite


class FavouriteListCreateAPIView(ListCreateAPIView):
    serializer_class = FavouriteListCreateSerializer
    pagination_class = FavouritePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    lookup_field = ('pk')
    permission_classes = [IsOwner]

