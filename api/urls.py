from django.urls import path,include
from .views import *
from .user_views import *

urlpatterns = [
     path('api/', SorovApiView.as_view()),
     # home
     path('hokim/',hokimpaneli,name='home'),
     path("hokim/1124424434354235412425/", hbarchasi, name="hammasi"),
     path('',hokimiyatPanel,name='hp'),
     # hps
     path('ars1/',filter_ariza_tur1,name='at1'),
     path('ars2/',filter_ariza_tur2,name='at2'),
     path('ars3/',filter_ariza_tur3,name='at3'),
     path('ars4/',filter_ariza_tur4,name='at4'),
     path('ars5/',filter_ariza_tur5,name='at5'),
     path('ars6/',filter_ariza_tur6,name='at6'),
     path('ars7/',filter_ariza_tur7,name='at7'),
     path('ars8/',filter_ariza_tur8,name='at8'),
     path('ars9/',filter_ariza_tur9,name='at9'),
     path('ars10/',filter_ariza_tur10,name='at10'),
     path('ars11/',filter_ariza_tur11,name='at11'),
     path('ars12/',filter_ariza_tur12,name='at12'),
     path('ars13/',filter_ariza_tur13,name='at13'),
     path('ars14/',filter_ariza_tur14,name='at14'),
     path('ars15/',filter_ariza_tur15,name='at15'),
     path('ars16/',filter_ariza_tur16,name='at16'),
     path('ars17/',filter_ariza_tur17,name='at17'),
     path('ars18/',filter_ariza_tur18,name='at18'),
     path('ars19/',filter_ariza_tur19,name='at19'),
     path('ars20/',filter_ariza_tur20,name='at20'),
     path('ars21/',filter_ariza_tur21,name='at21'),
     path('ars22/',filter_ariza_tur22,name='at22'),
     path('ars23/',filter_ariza_tur23,name='at23'),
     path('ars24/',filter_ariza_tur24,name='at24'),
     path('ars25/',filter_ariza_tur25,name='at25'),
     path('ars26/',filter_ariza_tur26,name='at26'),
     path('ars27/',filter_ariza_tur27,name='at27'),

     path('barchasi/',barcha,name='barchasi'),
     path('bajarilgan/',bajarilgan,name='bajarilgan'),
     path('md/',muddat,name='md'),
     path('bj/',bj,name='bj'),
     path('del/<int:id>',delete,name='del'),
     path('bja/<int:pk>',Change.as_view(),name='bja'),
     # user views-
     path('',include('django.contrib.auth.urls')),
     path('saiduwa/',CreateBlog.as_view(),name='new'),
     path('rahmat/',ramat,name='rahmat'),
     path('fwa/',fuwr,name='usw')
]