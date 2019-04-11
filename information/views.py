
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Presentation, Creator
from .serializers import PresentationSerializer
from rest_framework import filters


class PresentationListAPIView(ListAPIView):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ('createdAt',)
    permission_classes = (IsAuthenticated,)

    