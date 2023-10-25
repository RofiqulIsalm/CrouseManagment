from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from app.EmailBackEnd import EmailBackEnd
from app.models import CustormUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def Registration(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        # email chaking
        if User.objects.filter(email = email).exists():
            messages.warning(request, "Email Already Exists...!")
            return redirect('registration')
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username Already Exists...!')
            return redirect('registration')
        user = User(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, 'registration/logup.html')




def DoLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
		
        user = EmailBackEnd.authenticate(request,
                                        username=email,
                                        password=password)
        if user != None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request,'Email and Password Are not  valid...!')
            return redirect('login')
def Profile(request):
    return render(request, 'main/profile.html')

def ProfileUpdate(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')

@login_required(login_url='/')
def PasswordChange(request):
    if request.method == "POST":
        pwd = request.POST.get('cpwd')
        npwd = request.POST.get('npwd')
        
        try:
            custormuser = CustormUser.objects.get(id=request.user.id)
            cpwd = custormuser.check_password(pwd)
            if cpwd:
               custormuser.set_password(npwd)
               custormuser.save()
               messages.success(request, 'Password Change Successful...!')
            else:
               messages.error(request, 'Password Change faild...!')
        except CustormUser.DoesNotExist:
           messages.error(request, 'User not found...!')
        return redirect('profile')
    return render(request, 'registration/profile.html')

@login_required(login_url='/')
def PDetails(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        dateofbirth = request.POST.get('dateofbirth')
        address = request.POST.get('address')
        
        try:
            custormuser = CustormUser.objects.get(id = request.user.id)
            
            custormuser.first_name = first_name
            custormuser.last_name = last_name
            custormuser.phone = phone
            custormuser.date_of_birth = dateofbirth
            custormuser.address = address
            
            custormuser.save()
            messages.success(request,'Personal Details Update Successfully...!')
            return redirect('profile')
        except:
            messages.error(request,'Personal Details Update Failed...!')
            
    return render(request, 'registration/profile.html')

@login_required(login_url='/')
def Bio(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        
        try:
            custormuser = CustormUser.objects.get(id = request.user.id)
            
            custormuser.bio = bio
            custormuser.save()
            messages.success(request, 'Bio Update successfully...!')
            return redirect('profile')
        except:
            messages.error(request, 'Bio Update Failed...!')
    return render(request, 'registration/profile.html')

@login_required(login_url='/')
def Profile_photo(request):
    if request.method == 'POST':
        profile_photo = request.FILES.get('profilephoto')

        try:
            custormuser = CustormUser.objects.get(id=request.user.id)

            if profile_photo:
                custormuser.profile_photo = profile_photo
                custormuser.save()
                messages.success(request, 'Profile Photo Updated Successfully...!')
            else:
                messages.info(request, 'No file uploaded.')
        except CustormUser.DoesNotExist:
            messages.error(request, 'User not found.')
        return redirect('profile')
    return render(request, 'registration/profile.html')