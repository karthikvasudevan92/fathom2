from django.db import models

# Create your models here.
class Prefix(models.Model):
    name = models.CharField(max_length=10)
    factor = models.IntegerField()
    symbol = models.CharField(max_length=5, null=True)
    base = models.IntegerField(default=10)
    def __str__(self):
        return self.name
class Term(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Quantity(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True,null=True)
    bunit = models.ForeignKey('Unit',on_delete=models.CASCADE,related_name='quantity_unit',null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "quantities"
class Unit(models.Model):
    name = models.CharField(max_length=100)
    plural_name = models.CharField(max_length=100,null=True)
    desc = models.TextField(blank=True,null=True)
    quantity = models.ForeignKey(Quantity,on_delete=models.CASCADE,null=True)
    terms = models.ManyToManyField(Term,blank=True)
    coef = models.CharField(max_length=10)
    sig = models.IntegerField()
    def __str__(self):
        return self.name
