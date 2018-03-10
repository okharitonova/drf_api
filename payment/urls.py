from django.conf.urls import url
from .views import Account, Payment


urlpatterns = [
    url(r'^accounts/', Account.as_view()),
    url(r'^payments/', Payment.as_view()),
]
