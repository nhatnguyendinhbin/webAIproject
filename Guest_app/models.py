from django.db import models

# Create your models here.
class Type(models.Model):
    Type_ID = models.CharField(max_length = 150, default= "")
    Type_Name = models.CharField(max_length = 150, default= "")

    class Meta:
        db_table = 'Types'
        
    def __str__(self):
        return str(self.Type_Name)
    
# Create your models here.
class Manufacture(models.Model):
    Manufacture_ID = models.CharField(max_length = 150, default= "")
    Manufacture_Name = models.CharField(max_length = 150, default= "")

    class Meta:
        db_table = 'Manufactures'
        
    def __str__(self):
        return str(self.Manufacture_Name)

# Create your models here.
class Product(models.Model):
    Type_ID = models.ForeignKey(Type, on_delete=models.CASCADE)
    Manufacture_ID = models.ForeignKey(Manufacture, on_delete = models.CASCADE)
    Product_ID = models.CharField(max_length = 150, default= "") # Mã sản phẩm
    Product_Name = models.CharField(max_length = 150, default= "")# Tên sản phẩm
    Product_Img = models.ImageField(null=True, blank=True, upload_to="Images/")
    Configuration = models.CharField(max_length = 150, default= "")
    Description= models.CharField(max_length = 150, default= "") # Mô tả sản phẩm
    Quantity_In_Store = models.CharField(max_length = 150, default= "") # số lượng sản phẩm tồn kho
    Warranty = models.CharField(max_length = 150, default= "") #Chính sách bảo hành của sản phẩm
    Other = models.CharField(max_length = 150, default= "")
     
    class Meta:
        db_table = 'Products'
        
    def __str__(self):
        return str(self.Product_Name)
    
# Create your models here.
class Shopping_Cart(models.Model):
    Seasion_ID = models.CharField(max_length = 150, default= "")
    Quantity = models.CharField(max_length = 150, default= "")

    class Meta:
        db_table = 'Shopping_Carts'
        
    def __str__(self):
        return str(self.Quantity)
    
# Create your models here.
class OrderDetails(models.Model):
    Quantity = models.CharField(max_length = 150, default= "")
    Unit_Price = models.CharField(max_length = 150, default= "")

    class Meta:
        db_table = 'OrderDetails'
        
    def __str__(self):
        return str(self.Quantity)
    
# Create your models here.
class Promotions(models.Model):
    Pro_ID = models.CharField(max_length = 150, default= "")
    Pro_Name = models.CharField(max_length = 150, default= "")
    Pro_Des = models.CharField(max_length = 150, default= "")
    Pro_Picture = models.CharField(max_length = 150, default= "")
    Star_Date = models.CharField(max_length = 150, default= "")
    Endate = models.CharField(max_length = 150, default= "")

    class Meta:
        db_table = 'Promotions'
        
    def __str__(self):
        return str(self.Pro_Name)
    
