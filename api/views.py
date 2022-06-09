from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse



from .models import Bibita,Tessera,Colonna
from api.serializers import BibitaSerializer, TesseraSerializer, ColonnaSerializer

class BibitaViewSet(viewsets.ModelViewSet):

    queryset = Bibita.objects.all()
    serializer_class = BibitaSerializer
    permission_classes = [permissions.IsAuthenticated]


class TesseraViewSet(viewsets.ModelViewSet):

    queryset = Tessera.objects.all()
    serializer_class = TesseraSerializer
    permission_classes = [permissions.IsAuthenticated]


class ColonnaViewSet(viewsets.ModelViewSet):

    queryset = Colonna.objects.all()
    serializer_class = ColonnaSerializer
    permission_classes = [permissions.IsAuthenticated]

def eroga(request):
    eroga = "Bibita non erogata"
    bevanda = get_object_or_404(Bibita,pk=request.GET['bevanda'])
    tessera = get_object_or_404(Tessera,pk=request.GET['tessera'])
    creditofin=tessera.credito-bevanda.prezzo
    colonna= Colonna.objects.filter(bibita=bevanda.bevanda)
    for x in colonna:
        if x.numeroLatt>0:
            if tessera.credito > bevanda.prezzo:
                eroga=("Bibita ",x.bibita," erogata dalla colonna ",x.numeroCol,creditofin,x.numeroLatt)
                tessera.credito = creditofin
                tessera.save()
                x.numeroLatt=x.numeroLatt-1
                x.save()
                break
            else:
                eroga=("Credito insufficiente")
                break
        else:
                eroga=("Tutte le colonne di ",x.bibita," sono esaurite")


    return HttpResponse (eroga)