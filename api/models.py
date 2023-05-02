from django.db import models


class Sale(models.Model):
    hang = models.IntegerField(null=True, blank=True, verbose_name="Thứ hạng")
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name="Họ và tên")
    ma_gt = models.CharField(max_length=255, null=True, blank=True, verbose_name="Mã giới thiệu")
    sdt = models.CharField(max_length=255, null=True, blank=True, verbose_name="Số điện thoại")
    sl = models.IntegerField(null=True, blank=True, verbose_name="Số lượng khác")
    ky_gt = models.CharField(max_length=255, null=True, blank=True, verbose_name="Kỳ giới thiệu")

    def __str__(self):
        return self.ten + " - " + self.sdt


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Họ và tên")
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name="Số điện thoại")
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name="Email")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Địa chỉ")

    def __str__(self):
        return self.name + " - " + self.phone