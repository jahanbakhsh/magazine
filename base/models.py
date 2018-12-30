from django.db import models
from froala_editor.fields import FroalaField


class SubscriptionType(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    discount_fee = models.FloatField(help_text='فقط مقدار عددی میزان تخفیف را وارد کنید')
    currency = models.CharField(max_length=10)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Subscription Type"
        verbose_name_plural = "Subscription Type"


class Settings(models.Model):
    address = models.CharField("Address", max_length=150,help_text="آدرس دفتر مرکزی")
    telehphone = models.CharField("Telephone", max_length=15, help_text="تلفن دفتر مرکزی")
    email = models.EmailField("Email", help_text="ایمیل دفتر مرکزی")
    postalcode = models.CharField("PostalCode", max_length=12, help_text="کد پستی دفتر مرکزی")
    message = models.CharField(max_length=150)
    roles = FroalaField()
    class Meta:
        verbose_name = "Website Sttiings"
        verbose_name_plural = "Website Sttiings"


class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = FroalaField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)