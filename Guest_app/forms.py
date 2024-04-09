from django import forms
from . models import *

# form để checkout
class CustomerForm(forms.ModelForm):
    # chữ Meta nhớ viết hoa chữ M nếu không sẽ sai
    class Meta:
        model = Customer
        fields = ['Cust_Name', 'Cust_Adress', 'Cust_Phone','Cust_Email','Cust_Status']
        
        widgets = { #để định dạng form đăng nhập thông tin như trong css
                    'Cust_Name': forms.TextInput(attrs={'class': 'form-control'}),
                    'Cust_Adress': forms.TextInput(attrs={'class': 'form-control'}),
                    'Cust_Phone': forms.TextInput(attrs={'class': 'form-control'}),
                    'Cust_Email': forms.EmailInput(attrs={'class': 'form-control'}),
                    'Cust_Status': forms.TextInput(attrs={'class': 'form-control'}),
                    }



# form để chọn số lượng sản phẩm và cho vào giỏ hàng
class Order_DetailForm(forms.ModelForm):
    # chữ Meta nhớ viết hoa chữ M nếu không sẽ sai
    class Meta:
        model = Order_Detail
        fields = ['Quantity', 'Unit_Price']
        
        widgets = { #để định dạng form đăng nhập thông tin như trong css
                    'Quantity': forms.TextInput(attrs={'class': 'form-control'}),
                    'Unit_Price': forms.TextInput(attrs={'class': 'form-control'}),
                    }