from django.db import models


class Province(models.Model):
    THANH_PHO = 'Thành Phố'
    TINH = 'Tỉnh'
    TYPE_CHOICES = (
        (THANH_PHO, THANH_PHO),
        (TINH, TINH),
    )
    name = models.CharField(max_length=64)
    type = models.CharField(choices=TYPE_CHOICES, max_length=16)

    class Meta:
        unique_together = (('name', 'type'),)


class District(models.Model):
    QUAN = 'Quận'
    HUYEN = 'Huyện'
    THI_XA = 'Thị Xã'
    THANH_PHO = 'Thành Phố'
    TYPE_CHOICES = (
        (QUAN, QUAN),
        (HUYEN, HUYEN),
        (THI_XA, THI_XA),
        (THANH_PHO, THANH_PHO),
    )
    name = models.CharField(max_length=64)
    type = models.CharField(choices=TYPE_CHOICES, max_length=16)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    province = models.ForeignKey(Province, related_name='districts',
                                 on_delete=models.CASCADE)

    class Meta:
        unique_together = (('name', 'type', 'province'),)


class Ward(models.Model):
    PHUONG = 'Phường'
    THI_TRAN = 'Thị Trấn'
    XA = 'Xã'
    TYPE_CHOICES = (
        (PHUONG, PHUONG),
        (THI_TRAN, THI_TRAN),
        (XA, XA),
    )
    name = models.CharField(max_length=64)
    type = models.CharField(choices=TYPE_CHOICES, max_length=16)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    district = models.ForeignKey(District, related_name='wards',
                                 on_delete=models.CASCADE)

    class Meta:
        unique_together = (('name', 'type', 'district'),)
