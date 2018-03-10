from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    currency = models.CharField(max_length=3, default='PHP')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.balance.save()


class History(models.Model):
    from_account = models.ForeignKey(User, related_name='from_account', on_delete=models.PROTECT)
    to_account = models.ForeignKey(User, related_name='to_account', on_delete=models.PROTECT)
    amount = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    def __str__(self):
        return 'from: %s, to: %s, amount: %s' % (self.from_account.username,
                                                 self.to_account.username,
                                                 self.amount)

    class Meta:
        verbose_name = 'History'
        ordering = ('id',)
