from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Balance, History


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Balance
        fields = ('user', 'balance', 'currency')


class HistorySerializer(serializers.ModelSerializer):
    from_account = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    to_account = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = History
        fields = ('from_account', 'to_account', 'amount')
