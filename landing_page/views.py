from django.shortcuts import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseBadRequest
from django.template import loader
from .models import contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        print("!!!!!!!!!!!",email)
        message = request.POST.get('message')
        obj = contact.objects.create(name=name,contact_no=contact_no,
        email=email,message=message)
        print(obj)
        return redirect('/')
    return render(request,'index.html')


def contact_list(request):
    first_name = request.user.username
    data = contact.objects.all()
    context = {
    'first_name':first_name,
    'data':data
    }
    return render(request,'contact_list.html',context)


def delete_contact(request, pk):
    application = get_object_or_404(contact, pk=pk)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'deleted successfully')
        return redirect('/contact_list')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        i = request.user.id
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('contact_list')
        elif user is not None and not user.is_superuser:
            messages.error(request, 'invalid user')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'admin_login.html')
