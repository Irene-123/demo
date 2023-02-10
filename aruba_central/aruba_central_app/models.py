from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    created_by= models.ForeignKey(
        User, 
        related_name="%(class)s_createdby", 
        on_delete=models.CASCADE, 
        null=True 
    )
    updated_by= models.ForeignKey(
        User, 
        related_name="%(class)s_updatedby", 
        on_delete=models.CASCADE, 
        null=True, 
    )

    class Meta: 
        abstract=True 

class Site(BaseModel):
    site_id= models.IntegerField(primary_key=True)
    site_name= models.CharField(max_length=100, null=False)
    address= models.CharField(max_length=100, null=False)
    state= models.CharField(max_length=100, null=False)
    city= models.CharField(max_length=100, null=False)
    country= models.CharField(max_length=100, null=False)
    zipcode= models.IntegerField(null= True) 

    def __str__(self) -> str:
        return self.site_name
    
class order(BaseModel):
    status= (('Pending', 'Pending'), 
             ('In-transit', 'In-transit'), 
             ('Delivered', 'Delivered'))
    order_id= models.CharField(max_length=100,primary_key=True, null=False)
    purchase_id= models.CharField(max_length=100, null=False)
    quantity= models.CharField(max_length=100,null=False)
    type = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False, choices=status)

    def __str__(self) -> str:
        return self.order_id
    
class iap(BaseModel): 
    serial_no= models.CharField(max_length=100,primary_key=True, null= False)
    site_id= models.ForeignKey(Site, related_name='iappersite', on_delete=models.CASCADE)
    order_id= models.ForeignKey(order, related_name='iaporder', on_delete=models.CASCADE)
    ip_address= models.CharField(max_length=100, null= False)
    status= models.CharField(max_length=100, null= False)
    mac_address= models.CharField(max_length=100, null= False)
    is_vc= models.BooleanField(null= False)

    def __str__(self) -> str:
        return self.serial_no
    
class switch(BaseModel):
    site_id= models.ForeignKey(Site, related_name='switchpersite', on_delete=models.CASCADE)
    order_id= models.ForeignKey(order, related_name='switchorder', on_delete=models.CASCADE)
    serial_no= models.CharField(max_length=100,primary_key=True, null= False)
    ip_address= models.CharField(max_length=100, null= False)
    status= models.CharField(max_length=100, null= False)
    mac_address= models.CharField(max_length=100, null= False)

    def __str__(self) -> str:
        return self.serial_no
    


    



