from django.shortcuts import render, redirect
from .models import *
# thêm form
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'Guest_app/home.html')

# add product bằng adming của Django
# list phone:
def list_samsung(request):
    # Lọc các Type_ID là '1' (điện thoại)
    type_id = Type.objects.get(Type_ID='1')
    # chọn tất cả các sản phẩm sau khi được lọc
    samsung = Product.objects.filter(Type_ID=type_id, Manufacture='SAMSUNG')
    
    context= {'samsung':samsung, 'type_id': type_id }
    return render(request , 'Guest_app/dien_thoai/samsung/samsung.html',context)

def list_iphone(request):
    # Lọc các Type_ID là '1' (điện thoại)
    type_id = Type.objects.get(Type_ID='1')
    # chọn tất cả các sản phẩm sau khi được lọc
    iphone = Product.objects.filter(Type_ID=type_id, Manufacture='APPLE')

    context= {'iphone':iphone, 'type_id': type_id}
    return render(request , 'Guest_app/dien_thoai/iphone/iphone.html',context)


def list_xiaomi(request):
    # Lọc các Type_ID là '1' (điện thoại)
    type_id = Type.objects.get(Type_ID='1')
    # chọn tất cả các sản phẩm sau khi được lọc
    xiaomi = Product.objects.filter(Type_ID=type_id, Manufacture='XIAOMI')

    context = {'xiaomi':xiaomi, 'type_id': type_id}
    return render(request , 'Guest_app/dien_thoai/xiaomi/xiaomi.html',context)


# chi tiết sản phẩm theo id
def detail_product(request, id):
    detail_products = Product.objects.get(Product_ID=id)
    context = {'detail_products':detail_products}
    return render(request, 'Guest_app/detail_product.html', context)

# hiển thị danh sách hàng trong giỏ
def add_to_cart(request):
    if request.method == "POST":  
        form = Order_DetailForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                # return redirect('home')
            except:  
                pass
    else:  
        form = Order_DetailForm()
    context = {'form':form}
    return render(request, 'Guest_app/detail_product.html',context)

# hiển thị danh sách hàng trong giỏ
def add_to_cart(request):
    if request.method == "POST":  
        form = Order_DetailForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                # return redirect('home')
            except:  
                pass
    else:  
        form = Order_DetailForm()
    
    # Lấy chi tiết sản phẩm từ request hoặc từ database (phụ thuộc vào cách bạn gửi dữ liệu vào hàm view này)
    order_products = Order_Detail.objects.all() # Lấy thông tin sản phẩm tương ứng với request hoặc từ database

    context = {'form': form, 'order_products': order_products}
    return render(request, 'Guest_app/detail_product.html', context)



# check out
def check_out(request):  
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                return redirect('home')
            except:  
                pass
    else:  
        form = CustomerForm()  
    return render(request,'Guest_app/cart/check_out.html',{'form':form})

