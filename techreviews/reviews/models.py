from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
# Each model will become a table in the database
class TechType(models.Model):
    typename = models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='techtype'
    
class TechProduct(models.Model):
    productname=models.CharField(max_length=255)
    techtype=models.ForeignKey(TechType, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    entryDate=models.DateField()
    productURL=models.URLField()
    productdescription=models.TextField()

    def __str__(self):
        return self.productname
    
    class Meta:
        db_table='techproduct'

class TechReview(models.Model):
    reviewtitle=models.CharField(max_length=255)
    product=models.ForeignKey(TechProduct, on_delete=models.CASCADE)
    reviewdate=models.DateTimeField()
    reviewers=models.ManyToManyField(User)
    reviewrating = models.SmallIntegerField()
    reviewText = models.TextField()

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table='techreview'