"""regmysqlpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from regapp import views 
from regapp.views import adminreg,adminlog,userreg,printout,editdata,update,deletedata,pdf_convert,Viewpdf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('userreg/',views.home),  
    path('adminlog/pdf_convert',views.pdf_convert,name='pdf_convert'),
    
    path('adminlog/',views.adminlog,name='adminlog'),
    path('adminlog/userreg',views.userreg,name='userreg'),
    path('adminlog/userreg/adminreg',views.adminreg,name='adminreg'),
    path('adminlog/userreg/printout',views.printout,name='printout'),
    path('adminlog/editdata/<int:id>',views.editdata,name='editdata'),
    path('adminlog/update/<int:id>',views.update,name='update'),
    path('adminlog/deletedata/<int:id>',views.deletedata,name='deletedata'),
    
]
