from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# thêm form
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'Guest_app/home.html')

# add product bằng adming của Django
# list phone:
def list_iphone(request):
    # Lọc các Type_ID là '1' (điện thoại)
    type_id = Type.objects.get(Type_ID='1')
    # lọc theo id iphone =1
    manufacture_id = Manufacture.objects.get(Manufacture_ID='1')
    # chọn tất cả các sản phẩm sau khi được lọc
    iphone = Product.objects.filter(Type_ID=type_id, Manufacture_ID= manufacture_id )

    context= {'iphone':iphone, 'type_id': type_id,'manufacture_id':manufacture_id}
    return render(request , 'Guest_app/dien_thoai/iphone/iphone.html',context)

def list_samsung(request):
    # Lọc các Type_ID là '1' (điện thoại)
    type_id = Type.objects.get(Type_ID='1')
    # lọc theo id samsung = 2
    manufacture_id = Manufacture.objects.get(Manufacture_ID='2')
    # chọn tất cả các sản phẩm sau khi được lọc
    samsung = Product.objects.filter(Type_ID= type_id, Manufacture_ID= manufacture_id)
    
    context= {'samsung':samsung, 'type_id': type_id, 'manufacture_id':manufacture_id }
    return render(request , 'Guest_app/dien_thoai/samsung/samsung.html',context)

def list_xiaomi(request):
    # Lọc các Type_ID là '1' (điện thoại)
    type_id = Type.objects.get(Type_ID='1')
    # lọc theo id xiaomi = 3
    manufacture_id = Manufacture.objects.get(Manufacture_ID='3')
    # chọn tất cả các sản phẩm sau khi được lọc
    xiaomi = Product.objects.filter(Type_ID= type_id, Manufacture_ID= manufacture_id)

    context = {'xiaomi':xiaomi, 'type_id': type_id, 'manufacture_id':manufacture_id}
    return render(request , 'Guest_app/dien_thoai/xiaomi/xiaomi.html',context)

# chi tiết sản phẩm + thêm vào giỏ hàng
def detail_product(request, id):
    # Truy vấn sản phẩm dựa trên ID
    product = Product.objects.filter(Product_ID=id)
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        qty = int(request.POST.get('quantity', 1))
        
        # Tạo một đối tượng Shopping_Cart với thông tin sản phẩm và số lượng
        shopping_cart_item = Shopping_Cart(Product_ID_id=product_id, Quantity=qty)
        # Lưu đối tượng vào Shopping_Cart
        shopping_cart_item.save()
        return redirect('shopping_cart')
    
    context = {'product': product}
    return render(request, 'Guest_app/dien_thoai/detail_phone.html', context)

# hiển thị danh sách hàng trong giỏ hàng
@login_required(login_url='login')
def shopping_cart(request):
    list_shopping_cart = Shopping_Cart.objects.all()
    # Khởi tạo biến để tính tổng giá tiền
    total_price = 0
    
    # Duyệt qua từng mục trong giỏ hàng và tính tổng giá tiền
    for item in list_shopping_cart:
        # Tính tổng giá tiền cho mỗi mục
        total_price += item.Quantity * item.Product_ID.Unit_Price
        
    context = {'list_shopping_cart': list_shopping_cart,'total_price':total_price}
    return render(request, 'Guest_app/cart/shopping_cart.html', context)


# chi tiết đơn hàng trong giỏ
def order_detail(request):
    list_shopping_cart = Shopping_Cart.objects.all()
    orderdetails = Order_Detail.objects.filter(list_shopping_cart) 
    
    context = {'orderdetails': orderdetails, 'list_shopping_cart':list_shopping_cart}
    return render(request, 'Guest_app/cart/shopping_cart.html', context)

# xóa khỏi giỏ hàng
def remove_product(request, id):
    try:
        # Truy vấn mục trong giỏ hàng bằng id của nó
        shopping_cart_item = Shopping_Cart.objects.filter(id=id)
        # Xóa mục khỏi giỏ hàng
        shopping_cart_item.delete()
    except Shopping_Cart.DoesNotExist:
        # Xử lý trường hợp không tìm thấy mục trong giỏ hàng
        pass
    
    return redirect('shopping_cart')


# check out
def check_out(request):
    # checkout = Product.objects.get(Product_Name=id)
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
        
    context =  {'form': form}
    return render(request,'Guest_app/cart/check_out.html',context)

