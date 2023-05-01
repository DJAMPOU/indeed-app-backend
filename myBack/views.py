from rest_framework import generics
from .models import *
from .serializers import *

class PublicationView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class TypeView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class HRView(generics.ListAPIView):
    queryset = Horaires_Roulements.objects.all()
    serializer_class = HRSerializer

class PubliTypeView(generics.ListAPIView):
    queryset = Publi_Type.objects.all()
    serializer_class = PubliTypeSerializer    

class PubliHRView(generics.ListAPIView):
    queryset = Publi_HR.objects.all()
    serializer_class = PubliHRSerializer 