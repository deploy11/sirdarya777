from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Sorov(models.Model):
    fish = models.CharField(max_length=500,verbose_name='To`liq ismingizni kiriting?')
    idpassport = models.CharField(max_length=500,verbose_name='pasport seriasini kiriting')
    Yashashmanzili = models.CharField(max_length=500)
    
    mfynomi = models.CharField(max_length=500)
    kochanomi = models.CharField(max_length=500)
    telefonraqami = models.CharField(max_length=500)
    rasmvavidio = models.CharField(max_length=500)
    ariza_mazmuni = models.CharField(max_length=500)
    matn = models.TextField()

    def __str__(self) -> str:
        return self.fish
    
    def get_absolute_url(self):
        return reverse('rahmat')
class Orinbosar(models.Model):
    name = models.CharField(max_length=500)   
    def __str__(self) -> str:
        return self.name
class Tashkilotlar(models.Model):
    name = models.CharField(max_length=500)   
    def __str__(self) -> str:
        return self.name    

class Hokimiyat(models.Model):
    tel_name = models.CharField(max_length=500)
    orinbosar = models.ForeignKey(Orinbosar,on_delete=models.CASCADE,null=True)
    tashkilot = models.ForeignKey(Tashkilotlar,on_delete=models.CASCADE,null=True)
    muddat = models.DateField(auto_now_add=True)
    bajarildi = models.BooleanField(default=False,null=True)
    muddat_holati = models.BooleanField(default=False,null=True)

    def __str__(self) -> str:
        return self.murajat