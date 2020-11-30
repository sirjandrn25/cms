from django.db import models
from django.contrib.auth.models import Permission,PermissionsMixin,AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from college.managers.usermanager import UserManager
from django.contrib.auth.models import User

# Create your models here.




class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    object = UserManager()

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name +" "+self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active



class Profile(models.Model):
    select_gender = (
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    )
    avatar = models.ImageField(upload_to="profile/",default="default/default-user-img.png")
    bio = models.TextField(blank=True)
    birth_date = models.DateField(blank=True,null=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=150,choices=select_gender,default=1)
    location = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.user.email
