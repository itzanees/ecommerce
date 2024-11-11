from django.shortcuts import render,redirect,HttpResponse
from . forms import CategoryForm, ProductForm
from . models import Category, Product
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')

# category section
def category(request):
        categoryform = CategoryForm()
        savedCategory = Category.objects.all()
        if len(savedCategory)<1:
            error = 'Nothing in the list, create new'
            return render(request, 'category/category.html', {'categoryform': categoryform, 'savedCategory': savedCategory, 'error':error})
        return render(request, 'category/category.html', {'categoryform': categoryform, 'savedCategory': savedCategory})

def savecategory(request):
    try:
        if request.method == 'POST':
            categoryForm = CategoryForm(request.POST)
            if categoryForm.is_valid():
                categoryForm.save()
                message = "Category added."
                messages.success(request, message)
                return redirect('category')
            else:
                categoryForm = CategoryForm()
                message = "Category could not be created."
                show = {'message': message, 'categoryform':categoryForm}
                return redirect('category', show)
    except Exception as e:
        print("Error ", e)

def editcategory(request, ccode):
    catToEdit = Category.objects.filter(cat_code=ccode)
    try:
        if request.method =="POST":
            newcatcode = request.POST['new_cat_code']
            newname  = request.POST['new_name']
            if catToEdit.exists():
                message = "Category updated successfully."
                messages.success(request, message)
                catToEdit.update(cat_code = newcatcode, name = newname)
                return redirect('category')
        else:
            oldCat = Category.objects.get(cat_code = ccode)
            cat_name = oldCat.name
            return render(request, 'category/edit.html', {'catcode':ccode, 'old_name':cat_name})
    except Exception as e:
        print (e)

def deletecategory(request, ccode):
    catToDelete = Category.objects.get(cat_code=ccode)
    if request.method == "POST":
        catToDelete.delete()
        message = "Category deleted successfully"
        messages.success(request, message)
        return redirect('category')
    return render(request, 'category/delete.html', {'delete' :catToDelete})

# products section
def product(request):
    # category = Category().objects.all()
    product = Product.objects.all()
    if len(product) <1 :
        message = 'No items in the list'
        show_message = ''
        return render(request, 'products/products.html', {'products': product, 'message' : message} )
    show_message = 'd-none'
    return render(request, 'products/products.html', {'product': product, 'show_message':show_message} )

def addProduct(request):
    if request.method == "POST":
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            productForm.save()
            messages.success(request, "Product saved")
            return redirect('addproduct')
        else:
            messages.error(request, "Product not saved")
            return render(request, 'products/add.html', {'productform':productForm})
    productform = ProductForm()
    return render(request, 'products/add.html', {'productform':productform})

def editProduct(request, prodId):
    itemEdit = Product.objects.filter(id=prodId)
    try:
        if request.method == 'POST':
            name = request.POST['name']
            category  = request.POST['category']
            quantity = request.POST['quantity']
            price = request.POST['price']
            if itemEdit.exists():
                messages.success(request, "Product edited.")
                itemEdit.update(name = name, category= category, quantity =quantity, price = price)
                return redirect('products')
        else:
            form = ProductForm()
            return render(request, 'products/edit.html', {'form': form , 'values': itemEdit})
    except Exception as e:
        print(e)


def deleteProduct(request, prodId):
    itemDelete = Product.objects.get(id=prodId)
    if request.method == "POST":
        itemDelete.delete()
        message = f'{itemDelete.name} Deleted Successfully'
        messages.success(request, message)
        return redirect('products')
    
    return render (request, 'products/delete.html', {'item' : itemDelete.name})


# AUTHENTICATION

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"registration/login.html",{"msg":"Invalid login"})

def logout_view(request):
    logout(request)
    return redirect('login')



def signup(request):
    try:
        if request.method == "POST":
            xform = UserCreationForm(request.POST)
            if form.is_valid():   
                form.save() 
                return redirect('login')  
            return render(request, 'registration/signup.html', {'form': form,'msg':'Invalid details'})       
        else:
            form=UserCreationForm()
            return render(request, 'registration/signup.html', {'form': form})
    except Exception as e:
            print(e)
            userform = UserCreationForm()
            return render(request, 'registration/signup.html', {'form': form})
    


def passwordreset(request):
    if request.method == "POST":
        uname = request.POST['username']
        newpwd1=request.POST['password1']
        newpwd2=request.POST['password2']
        try:
            if newpwd1 == newpwd2:
                user=User.objects.get(username=uname)
                if user is not None:
                    user.set_password(newpwd1)
                    user.save()
                return render(request,"registration/ResetPassword.html",{"msg":"Password Reset Successfully"})
            else:
                return render(request,"registration/ResetPassword.html",{"msg":"Passwords do not match"})
        except Exception as e:
            print(e)
            return render(request,"registration/ResetPassword.html",{"msg":"Password Reset Failed"})
    return render(request,'registration/ResetPassword.html')
