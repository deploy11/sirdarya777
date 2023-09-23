from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from django.utils import timezone
from rest_framework.generics import *
from django.views.generic import *
from .forms import DweetForm
from django.views.generic.edit import UpdateView
class SorovApiView(ListCreateAPIView):
    queryset = Sorov.objects.all()
    serializer_class  = SorovSerializer

def hokimpaneli(request):
    if request.user.username == 'admin':
        hammasi = Sorov.objects.all().count()
        bajargan = Hokimiyat.objects.filter(bajarildi=True).count()
        bajarilmagan = Hokimiyat.objects.filter(bajarildi=False).count()
        muddati_otkan = Hokimiyat.objects.filter(muddat_holati=True).count()
        return render(request,'hokim.html',{
            'hammasi':hammasi,
            'bajargan':bajargan,
            'bajarilmagan':bajarilmagan,
            'muddati_otkan':muddati_otkan
        })
    else:
        return redirect('login')
def hbarchasi(request):
    
    hammasis = Sorov.objects.all()
    return render(request,'barcha.html',{
        'hammasi':hammasis,
    })

def ramat(request):
    return render(request,'rahmat.html')

class CreateBlog(CreateView):
    model = Hokimiyat
    template_name = 'blog_new.html'
    fields = ('__all__')

def hokimiyatPanel(request):
    if request.user.is_authenticated: 
        if request.user.is_staff == False:
            hok = Hokimiyat.objects.filter(bajarildi=False)
            ariza = Sorov.objects.all()
            return render(request,'hp2.html',{'hok':hok,'ariza':ariza})
        hammasi = Sorov.objects.all().count()
        bajargan = Hokimiyat.objects.filter(bajarildi=True).count()
        bajarilmagan = Hokimiyat.objects.filter(bajarildi=False).count()
        muddati_otkan = Hokimiyat.objects.filter(muddat_holati=True).count()
        ariza = Sorov.objects.all()
        
        return render(request,'hp.html',{
            'hammasi':hammasi,
            'bajargan':bajargan,
            'bajarilmagan':bajarilmagan,
            'muddati_otkan':muddati_otkan,
            'ariza':ariza
        })
   
    else:
        return redirect('login')
    
def barcha(request):
    
    ariza = Sorov.objects.all()
    return render(request,'barcha.html',{'ariza':ariza})
def bajarilgan(request):
    ariza = Hokimiyat.objects.filter(bajarildi=True)
    return render(request,'bajarilgan.html',{'ariza':ariza})
def muddat(request):
    ariza = Hokimiyat.objects.filter(muddat_holati=True)
    return render(request,'md.html',{'ariza':ariza})
def bj(request):
    ariza = Hokimiyat.objects.filter(bajarildi=False)
    return render(request,'bj.html',{'ariza':ariza})
def tash(request):
    if request.user.username == 'tash1':
        ariza = Hokimiyat.objects.filter(tashkilot='t1')
    elif request.user.username == 'tash2':
        ariza = Hokimiyat.objects.filter(tashkilot='t1')

def delete(request,id):
    Sorov.objects.filter(id=id).delete()
    return redirect('hp')
class Change(UpdateView):
    model = Hokimiyat
    template_name = 'bajar.html'
    fields = ['bajarildi']
def filter_ariza_tur1(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    hokimiyat = Hokimiyat.objects.all()
    ariza = Sorov.objects.filter(ariza_mazmuni='суд  масалалари')
    return render(request,'hp_az/hp_az1.html',{'ariza':ariza,"form": form,'hokimiyat':hokimiyat})
def filter_ariza_tur2(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='ички ишлар  фаол.')
    return render(request,'hp_az/hp_az2.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur3(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='прокуратура фаол. оид')
    return render(request,'hp_az/hp_az3.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur4(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='алимент масаласи')
    return render(request,'hp_az/hp_az4.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur5(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='суд  ижросига оид')
    return render(request,'hp_az/hp_az5.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur6(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='соғлиқни сақлаш')
    return render(request,'hp_az/hp_az6.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur7(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='пенсия ва нафақа')
    return render(request,'hp_az/hp_az7.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur8(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni=' мактаб  таълими')
    return render(request,'hp_az/hp_az8.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur9(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='уй-жой, ер б-н таъм.')
    return render(request,'hp_az/hp_az9.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur10(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='иш б-н таъминлаш')
    return render(request,'hp_az/hp_az10.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur11(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='афв этиш масаласи')
    return render(request,'hp_az/hp_az11.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur12(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='олий таълим масалалариa')
    return render(request,'hp_az/hp_az12.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur13(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='кредит олиш')
    return render(request,'hp_az/hp_az13.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur14(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='банк-молия  масалалари')
    return render(request,'hp_az/hp_az14.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur15(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='газ, электр, сув, иссиқлик таъминоти')
    return render(request,'hp_az/hp_az15.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur16(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='коммунал тўловларни ҳисоблаш')
    return render(request,'hp_az/hp_az16.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur17(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='йўл қурилиши')
    return render(request,'hp_az/hp_az17.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur18(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='солиқ  тўловлари')
    return render(request,'hp_az/hp_az18.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur19(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='транспорт масалалари')
    return render(request,'hp_az/hp_az19.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur20(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='қурилиш  соҳаси')
    return render(request,'hp_az/hp_az20.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur21(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='тадбиркорлик  ҳуқукларини бузулиши  ')
    return render(request,'hp_az/hp_az21.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur22(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='санъ-ат, маърифат ва маданият масалалари')
    return render(request,'hp_az/hp_az22.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur23(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='дори-дармонга нарх-наво масаласи')
    return render(request,'hp_az/hp_az23.html',{'ariza':ariza,"form": form,})


def filter_ariza_tur24(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='биринчи эҳтиёж молларига нарх-наво масалалари')
    return render(request,'hp_az/hp_az24.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur25(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='давлат хизмати фаолияти')
    return render(request,'hp_az/hp_az25.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur26(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='моддий  ёрдам  олиш')
    return render(request,'hp_az/hp_az26.html',{'ariza':ariza,"form": form,})

def filter_ariza_tur27(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            
    form = DweetForm()
    ariza = Sorov.objects.filter(ariza_mazmuni='бошқа масалалар')
    return render(request,'hp_az/hp_az28.html',{'ariza':ariza,"form": form,})
def fuwr(request):
    return render(request,'uls.html')