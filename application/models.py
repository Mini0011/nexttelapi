from django.utils import timezone
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
 
#user ou developpeur ou consommateur du l'api

class MyUser(AbstractBaseUser):
    
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    ###
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
   
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

class tokens(models.Model):
    accesskey = models.CharField(max_length=120, unique=True)
    expirydate = models.DateTimeField()
    user = models.ForeignKey(MyUser, related_name='user_token', on_delete=models.CASCADE)
    
# l'application qui client a 
class Applications_clientes(models.Model):
    nom = models.CharField(max_length=200,unique=True)
    type_application =models.CharField(max_length=200)
    user=models.ForeignKey(MyUser, related_name='applications_clientes', on_delete=models.CASCADE)
    description =models.CharField(max_length=200)

# services du l'api recharge ou sms ou ussd
class Service(models.Model):
    operateur = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    libelle= models.CharField(max_length=200)
    date_effectue = models.DateTimeField(default=timezone.now)
    destinataire = models.IntegerField()
    emetteur = models.IntegerField()
    
class Recharge(Service):
    #recharge
    pass
    
class Messages(Service):
    #sms
    pass

#client doit abonner a l'api pour utiliser
class Abonnement(models.Model):
    montant_credit =models.IntegerField(blank=True, null=True)
    nbre_sms =models.IntegerField(blank=True, null=True)
    application_cliente_id =models.OneToOneField(Applications_clientes, related_name='abonnement', on_delete=models.CASCADE,unique=True)
    service_id =models.ManyToManyField(Service, related_name='s_abonner')