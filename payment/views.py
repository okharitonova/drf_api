from .models import Balance, History
from .serializers import AccountSerializer, HistorySerializer

from rest_framework import mixins, generics


class Account(generics.ListAPIView):
    queryset = Balance.objects.all()
    serializer_class = AccountSerializer


class Payment(generics.ListCreateAPIView):
    """
    List all users with balance.
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer
