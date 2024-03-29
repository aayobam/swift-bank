from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse

from apis.common import choices
from apis.common.custom_validator import file_validator, verify_date_of_birth
from apis.common.models import TimeStampedModel
from apis.users.managers import CustomUserManager


class CustomUser(AbstractUser, TimeStampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(default="male", choices=choices.GENDER, max_length=10)
    role = models.CharField(default="admin", choices=choices.ROLE, max_length=50)
    phone_no = models.CharField(max_length=11)
    birth_date = models.DateField(blank=True, null=True)
    age = models.CharField(max_length=4, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(
        default="nigeria", choices=choices.COUNTRY, max_length=100)
    profile_picture = CloudinaryField(
        "profile_images", validators=[file_validator], blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        ordering = ("-date_created",)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"user_id": self.id})

    def __unicode__(self):
        try:
            public_id = self.profile_picture.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)

    def save(self, *args, **kwargs):
        self.age = verify_date_of_birth(self.birth_date)
        return super().save(*args, **kwargs)
