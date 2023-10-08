
from django.contrib import admin
from django.urls import path,include
from . import views,user_log
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.Base, name="base"),
    path('',views.Home, name="homepage"),
    path('404', views.PageNotFound, name="404"),
    path('courses',views.SingleCourse, name="singlecourse"),
    path('courses/filter-data',views.filter_data,name="filter-data"),
    path('course/<slug:slug>', views.CourseDetails, name="coursedetails"),
    path("search", views.query_course, name="query_course"),
    path('about/',views.About, name="about"),
    path('contact/',views.Contact, name="contact"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration',user_log.Registration, name="registration"),
    path('accounts/registration/teacher',user_log.RegistrationT, name="registrationteacher"),
    path('dologin',user_log.DoLogin, name='dologin'),
    path('accounts/profile',user_log.Profile, name='profile'),
    path('accoutns/profile/update',user_log.ProfileUpdate, name="profile_update"),
    path('chackout/<slug:slug>',views.Chackout,name="chackout"),
    path('my-course/', views.MyCourse,name='my_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('course/watch-course/<slug:slug>', views.WatchCourse,name='watch_course'),
    path('payment-varification/', views.PaymentVarification,name='PaymentVarification'),
    path('create_course/', views.create_course, name='create_course'),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
