from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE


class MyAccountManager(BaseUserManager):

    def create_user(self, name,email,mobile_number,role,password=None):
        if not email:
            raise ValueError("users must have an email address. ")
        if not mobile_number:
            raise ValueError("users must have a mobile number. ")
        
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            mobile_number = mobile_number,
            role = role,
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, name, email, mobile_number, role, password=None):
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            mobile_number = mobile_number,
            role = role
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self.db)
        return user




class Account(models.Model):

    role                = models.CharField(max_length=50)
    company_name        = models.CharField(max_length=250)

    def __str__(self):
        return self.role + "/ " + self.company_name




class Users(AbstractBaseUser):

    name                = models.CharField(max_length=250)
    email               = models.EmailField(unique=True)
    mobile_number       = models.CharField(max_length=250,unique=True)
    role                = models.ForeignKey(Account, on_delete=CASCADE)
    date_joined         = models.DateField(auto_now_add=True)
    last_login          = models.DateField(auto_now=True)
    is_active           = models.BooleanField(default=True)
    is_superuser        = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)

    USERNAME_FIELD      = 'email'
    REQUIRED_FIELDS      = ['mobile_number','name']

    objects = MyAccountManager()

    def __str__(self):
        return self.name +'/' + self.email
    
    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

class Invite(models.Model):

    email               = models.EmailField(unique=True)
    role                = models.ForeignKey(Account, on_delete=CASCADE)


    def __str__(self):
        return self.email



