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
class Product(models.Model):
    Type_ID = models.ForeignKey(Type, on_delete = models.CASCADE)  # khóa ngoài với Type
    Manufacture = models.CharField(max_length = 150, default= "")
    Product_ID = models.CharField(max_length = 150, default= "")
    Product_Img = models.ImageField(null=True, blank=True, upload_to="Images/")
    Product_Name = models.CharField(max_length = 150, default= "")
    Configuration = models.CharField(max_length = 150, default= "")
    Description= models.CharField(max_length = 500, default= "")
    Quantyti_In_Store = models.CharField(max_length = 150, default= "")
    Unit_Price = models.CharField(max_length = 150, default= "")
    Warranty = models.CharField(max_length = 150, default= "")
    Other = models.CharField(max_length = 150, default= "")
     
    class Meta:
        db_table = 'Products'
        
    def __str__(self):
        return str(self.Product_Name)
    
    
# Create your models here.
class Order_Detail(models.Model):
    Product_Name = models.ForeignKey(Product, on_delete = models.CASCADE)  # khóa ngoài với Product
    Quantity = models.CharField(max_length = 150, default= "")
    Unit_Price = models.CharField(max_length = 150, default= "")

    class Meta:
        db_table = 'Order_Details'
        
    def __str__(self):
        return str(self.Quantity)
    
# Create your models here.
class Shopping_Cart(models.Model):
    Seasion_ID = models.CharField(max_length = 150, default= "")
    Quantity = models.ForeignKey(Order_Detail, on_delete = models.CASCADE)  # khóa ngoài với Order_Detail

    class Meta:
        db_table = 'Shopping_Cart'
        
    def __str__(self):
        return str(self.Quantity)

# Create your models here.
class Customer(models.Model):
    Cust_ID = models.CharField(max_length = 150, default= "")
    Cust_Name = models.CharField(max_length = 150, default= "")
    Cust_Adress = models.CharField(max_length = 150, default= "")
    Cust_Phone = models.CharField(max_length = 150, default= "")
    Cust_Email = models.CharField(max_length = 150, default= "")
    Cust_Password = models.CharField(max_length = 150, default= "")
    Cust_Status = models.CharField(max_length = 150, default= "")
    
    class Meta:
        db_table = 'Customer'
        
    def __str__(self):
        return str(self.Quantity)

# Create your models here.
class User(models.Model):
    User_ID = models.CharField(max_length = 150, default= "")
    Role = models.CharField(max_length = 150, default= "")
    User_Name = models.CharField(max_length = 150, default= "")
    PassWord = models.CharField(max_length = 150, default= "")
    Status = models.CharField(max_length = 150, default= "")
    
    class Meta:
        db_table = 'User'
        
    def __str__(self):
        return str(self.User_Name)
