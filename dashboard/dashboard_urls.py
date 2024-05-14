from django.urls import path
from dashboard.views import DashView,ReportCase,SubmitView,StatView,UserDashView

urlpatterns=[
     path('userdash/', UserDashView, name='userdash'),
     path('dashboard', DashView, name='dashboard'),
     path('statistics/', StatView, name='statistics'),
     path('reportcase/',ReportCase,name='reportcase'),
     path('submit',SubmitView,name='submitform')
]