from django.shortcuts import render,redirect
from app.models import Categories,Course,Lavel,Video,UserCourse,Payment
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages
from time import time

def Base(request):
    return render(request, 'base.html')

def Home(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    context = {
        'category' : category,
        'course' : course,
    }
    return render(request, 'main/home.html', context)

def SingleCourse(request):
    category = Categories.get_all_category(Categories)
    lavel = Lavel.objects.all()
    course = Course.objects.all()
    freeCourse_count = Course.objects.filter(price = 0).count()
    paidCourse_count = Course.objects.filter(price__gte=1).count()
    context = {
        'category': category,
        'lavel' : lavel,
        'course': course,
        'freeCourse_count' : freeCourse_count,
        'paidCourse_count' : paidCourse_count,
        
    }
    
    return render(request, 'main/single_course.html', context)
def filter_data(request):
    category = request.GET.getlist('category[]')
    lavel = request.GET.getlist('lavel[]')
    price = request.GET.getlist('price[]')
    
    if price == ['PriceFree']:
        course = Course.objects.filter(price=0)
    elif price ==['PaicePaid']:
        course = Course.objects.filter(price__gte=1)
    elif price == ['PaiceAll']:
        course = Course.objects.all()
    elif category:
        course = Course.objects.filter(category__id__in = category).order_by('-id')
    elif lavel:
        course = Course.objects.filter(lavel__id__in = lavel).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')
    context = {
        'course' : course,
        
    }
    t = render_to_string('ajax/course.html',context)

    return JsonResponse({'data': t})
def query_course(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    
    context = {
        'course' : course,
    }
    return render(request, 'query/query.html', context)
def About(request):
    category = Categories.get_all_category(Categories)
    
    context = {
        'category' : category,
    }
    return render(request, 'main/about.html', context)
def Contact(request):
    category = Categories.get_all_category(Categories)
    
    context = {
        'category' : category,
    }
    return render(request, 'main/contact.html', context)

def CourseDetails(request,slug):
    category = Categories.get_all_category(Categories)
    time_duration = Video.objects.filter(course__slug = slug).aggregate(sum = Sum('time_duration'))
    course_id = Course.objects.get(slug = slug)
    try:
        chack_enroll = UserCourse.objects.get(user = request.user , course = course_id)
    except UserCourse.DoesNotExist:
        chack_enroll = None
    course = Course.objects.filter(slug = slug)
    
    if course.exists:
        course = course.first()
    else:
        return redirect('404')
    
    context ={
        'category' : category,
        'course': course,
        'time_duration' : time_duration,
        'chack_enroll' : chack_enroll,
    }
    return render(request, 'component/course/coursedeteils.html', context)

def PageNotFound(request):
    category = Categories.get_all_category(Categories)
    
    context = {
        'category' : category,
    }
    return render(request, 'component/error/404.html', context)

def Chackout(request,slug):
    course = Course.objects.get(slug = slug)
    action = request.GET.get('action')
    order = None
    if course.price == 0:
        course = UserCourse(
            user = request.user,
            course = course,
        )
        course.save()
        messages.success(request,'Course Are successfuly enroll...!')
        return redirect('my_course')
    elif action == 'create_payment':
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            city = request.POST.get('city')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            order_comments = request.POST.get('order_comments')
            
            amount = course.price * 100
            currency = "BDT"
            note = {
                "name" : f'{first_name} {last_name}',
                "city" : city,
                "phone": phone,
                "email": email,
                "order_comments": order_comments,
            }
            receipt = f"SchoolManagmenet-{int(time())}"
            payment = Payment(
                course = course,
                user = request.user,
            )
            
    context = {
        'course':course,
    }
    return render(request, 'chackout/chackout.html', context)
    
def MyCourse(request):
    course = UserCourse.objects.filter(user = request.user)
    
    context = {
        'course':course,
    }
    return render(request, 'component/course/my_course.html',context)

def PaymentVarification(request):
    return render(request, "Chackout/payment.html")