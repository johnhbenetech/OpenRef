from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.timezone import now


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
		
def validate_state(value):
    if value not in ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY', 'AE', 'AA', 'AP']:
        raise ValidationError(u'%s is not a valid state abbreviation' % value)	


class Provider(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    street_address2 = models.CharField(max_length=50,null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2,validators=[validate_state])
    zipcode = models.CharField(max_length=5)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    owner = models.ForeignKey('auth.User', related_name='author', on_delete=models.CASCADE, null=True)
    

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return "%s %s \xa0\xa0 %s %s, %s, %s \xa0\xa0 %s \xa0\xa0\xa0 (last updated: %s)" % (self.first_name, self.last_name, self.street_address, self.street_address2, self.city, self.state, self.zipcode, self.updated_date)
	
	
class Update(models.Model):
    provider_id = models.ForeignKey(Provider, models.SET_NULL, blank=True, null=True,)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    street_address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    

    class Meta:
        verbose_name = "Update"
        verbose_name_plural = "Updates"

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.provider_id, self.first_name, self.last_name, self.street_address, self.street_address2, self.city, self.state, self.zipcode, self.updated_date)