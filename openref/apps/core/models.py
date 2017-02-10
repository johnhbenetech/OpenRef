from django.db import models

class Provider(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    street_address2 = models.CharField(max_length=50,null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    updated_date = models.DateField()
    

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s' % (self.first_name, self.last_name, self.street_address, self.street_address2, self.city, self.state, self.zipcode, self.updated_date)

class Update(models.Model):
    provider_id = models.ForeignKey(Provider, models.SET_NULL, blank=True, null=True,)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    street_address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    updated_date = models.DateField()
    

    class Meta:
        verbose_name = "Update"
        verbose_name_plural = "Updates"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.provider_id, self.first_name, self.last_name, self.street_address, self.street_address2, self.city, self.state, self.zipcode, self.updated_date)