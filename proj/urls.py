
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static

urlpatterns = [
#WebPages
    path('admin/',admin.site.urls),
    

    path('adminart', views.oragnizerLogin,name="adminart"),
    path('', views.index,name="home"),
    path('blog', views.blogs,name="blogs"),
    # path('adminart', views.admin,name="adminart"),
    path('single-standard.html', views.vg,name="single-standard.html"),
    path('blog/<id>', views.blogroute,name="blogroute"),
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings)