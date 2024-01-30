from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Song.objects.filter(album_id=pk)
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        if self.request.user.is_authenticated:
            album = get_object_or_404(Album, pk=pk)
            serializer.save(album=album)