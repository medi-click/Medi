from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404

from .models import *
from django.db.models import Q
#from .utils import cartData, cookieCart
from .forms import UserCreationForm,UpdateUserProfileForm,ProductForm

from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from .forms import *

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash



from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def iregister(request):
    if request.method=="POST":
    
        form=UserCreationForm(request.POST)
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password1"]
        Login_as=request.POST["login_field"]
        print(username,email,password,Login_as)  
        user=User.objects.create(username=username,email=email)
        user.set_password(password)
        grp=Group.objects.get(name=Login_as)
        user.groups.add(grp) 
        # if grp==customer:
        #     customer.permissions.set[]

        user.save()    
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, 'Account created successfully')
        #     return redirect('register')
        
    else:
        form=UserCreationForm()
    return render(request,"iregister.html",{'form':form})    
   
def isignin(request):
    if not request.user.is_authenticated:

        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data["username"]
                upass=fm.cleaned_data["password"]
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    
                    # if user.groups.filter(name="Customer"):
                        
                    #print(user.groups)
                    #     login(request,user)
                    #     return redirect("/customer/")
                    # else:
                    #     if user.groups.filter(name="Retailer"):
                    
                    #         #print(user.groups)
                    #         login(request,user)
                    #         return redirect("/retailer/")
                    #     else:
                    #         login(request,user)
                    #         return redirect("/wholesaler/")
                    login(request,user)
                    # print(request.user.groups)
                    return redirect("/profile/")

                else:
                    return redirect('/signin/')
        
        else:
            fm=AuthenticationForm()
        return render(request,'isignin.html',{'form':fm})

    else:
        # if user.groups.filter(name="Customer"):
        #     return redirect('/customer/')
        # else:
        #     if user.groups.filter(name="Retailer"):
        #         return redirect('/retailer/')
        #     else:
        #         return redirect('/wholesaler/')
        return redirect('/profile/')


def iprofile(request):
    if request.user.is_authenticated:
        
        return render(request,"iprofile.html")
    else:
        return redirect('/signin/')
   
def isignout(request):                                
    logout(request)
    return redirect('/signin/')


def ichangepass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return redirect('/profile/')

        else:
            fm =PasswordChangeForm(user=request.user )
        return render(request,"ichangepass.html",{'form':fm})

    else:
        return redirect('/signin/')


def inewpass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return redirect('/profile/')

        else:
            fm =SetPasswordForm(user=request.user )
        return render(request,"newpass.html",{'form':fm})

    else:
        return redirect('/signin/')

def ipasswordreset(request):
   
    if request.method=="POST":
         fm=PasswordResetForm(request.POST)
         if fm.is_valid():
             fm.save(from_email=mediclick1@gmail.com)

    else:
        fm=PasswordResetForm()
        return render(request,"ipasswordreset.html",{'form':fm})

def iupdateprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=UpdateUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
        else:
            fm=UpdateUserProfileForm(instance=request.user)
        return render(request,"iupdateprofile.html",{'form':fm})
    else:
        return redirect('/profile/')

def customer(request): 
    return render(request,"customer.html")


def retailer(request):
    return render(request,"retailer.html")


def wholesaler(request):
    return render(request,"wholesaler.html")


def iproducts(request):
    return render(request,'shop-04-column.html')

def iadd_stock(request):
    if request.user.is_authenticated:
        if  request.method=="POST":
            form=ProductForm(request.POST)
            if form.is_valid():
                form=form.save(commit=False)
                form.user=request.user
                form.save()
                return redirect('addstock')
        else:
            form=ProductForm()
            return render(request,'iaddstock.html',{'form':form})
    else:
        return redirect('/signin/')

def isearchresults(request):
    query=request.GET.get('S')
   
    b=Product.objects.filter(
        medicine_name__icontains=query
    )
  
    return render(request,'isearchresults.html',{"b":b})







################################################################################################################################################
#E-comm
# def registerPage(request):
# 	form = CreateUserForm()
# 	if request.method =='POST':
# 		form = CreateUserForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			user = form.cleaned_data.get('username')
# 			#print("@@@@@@@@@@@@@@@@@",user)
# 			messages.success(request,'Account was created for '+ user)
# 			return redirect('login')
# 	context ={'form':form}
# 	return render(request,'register.html',context)

def loginPage(request):
	if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')

			else:
				messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request,'login.html',context)

def logoutPage(request):
	logout(request)
	return redirect('login')
'''
def reset(request):
	if request.method =='POST':
		message = request.POST['message']
		send_mail(subject, message, settings.EMAIL_HOST_USER, ['rutvapatel2000@gmail.com'], fail_silently=False)
		return render(request, 'reset.html')
'''


def index_view(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items =[]
		order = {'get_cart_total': 0, 'get_cart_items':0}
		cartItems = order['get_cart_items']
	products = Product.objects.all()
	comment = Category.objects.all()
	
	#print("products:",Product)
	#print('context:',context)
	context = {'products':products, 'cartItems':cartItems, 'comment':comment}

	return render(request,'index.html',context)

def product_details_view(request,pk):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items =[]
		order = {'get_cart_total': 0, 'get_cart_items':0}
		cartItems = order['get_cart_items']
	
	products = Product.objects.get(id=pk)

	context = {'products':products, 'items':items, 'order':order,'cartItems':cartItems}
	
	return render(request, 'product_details.html', context)

def category_view(request,pk):
	cat = Category.objects.filter(id=pk)
	pro = Product.objects.filter(categories=cat[0].id)
	comment = Category.objects.all()
	# print('cat:',cat)
	# print('pro:',pro)
	
	context ={'cat':cat,'pro':pro, 'comment':comment}
	return render(request,'category.html',context)

def about_view(request):
    return render(request,'about.html')

def cart_view(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items =[]
		order = {'get_cart_total': 0, 'get_cart_items':0}
		cartItems = order['get_cart_items']
	context = {'items':items, 'order':order,'cartItems':cartItems}
	return render(request,'cart.html',context)

def wishlist_view(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer)
		item = order.wishitem_set.all()
		#print('b:',item)
		cartItems = order.get_cart_items
	else:
		item =[]
		order = {'get_cart_total': 0, 'get_cart_items':0}
		cartItems = order['get_cart_items']
	context = {'item':item, 'order':order,'cartItems':cartItems}
	return render(request,'wishlist.html',context)

def checkout_view(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		#print("item:",items)
	else:
		items =[]
		order = {'get_cart_total': 0, 'get_cart_items':0}
		cartItems = order['get_cart_items']
		
	form = ShippingForm()
	if request.method =='POST':
		form = ShippingForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/paypal')
			except:
				pass
		else:
			form=ShippingForm()
	context = {'form':form,'items':items, 'order':order,'cartItems':cartItems}
	
	
	return render(request,'checkout.html',context)

def paypal(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		
	else:
		items =[]
		order = {'get_cart_total': 0, 'get_cart_items':0}
		cartItems = order['get_cart_items']
	context = {'items':items, 'order':order,'cartItems':cartItems}
	return render(request,'paypal.html',context)



def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('productId:',productId)
	print('Action:',action)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action =='remove1':
		orderItem.quantity = 0
	else:
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <=0:
		orderItem.delete()
	return JsonResponse('Item was added', safe=False)

def siteView(request):
	return render(request,'site.html')

def wishItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('productId:',productId)
	print('Action:',action)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer)

	wishItem, created = WishItem.objects.get_or_create(order=order, product=product)
	
	if action == 'add':
		wishItem.quantity_wish = 1
		print('add:',wishItem.quantity_wish)
	else:
		wishItem.quantity_wish = 0
		print('remove:',wishItem.quantity_wish)
	

	wishItem.save()

	if wishItem.quantity_wish <=0:
		wishItem.delete()
	
	#print('a:',wishItem)
	#wishItem.save()
	return JsonResponse('Item was added in wish', safe=False)


def search(request):
	query=None
	results=[]
	if request.method=="POST":
		query=request.POST.get('search')
		results = Product.objects.filter(name=query)
		# results=Product.objects.filter(Q(name__icontains=query) | Q(manufacturered_by__icontains=query) | Q(categories__icontains=query) )
		print(results)
	return  render(request,'search.html',{'query': query,
                                          'results': results})