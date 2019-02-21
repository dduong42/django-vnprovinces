# Generated by Django 2.1.4 on 2019-02-21 03:11

from django.db import migrations

provinces = (
    ('Hà Nội', 'Thành Phố'),
    ('Hà Giang', 'Tỉnh'),
    ('Cao Bằng', 'Tỉnh'),
    ('Bắc Kạn', 'Tỉnh'),
    ('Tuyên Quang', 'Tỉnh'),
    ('Lào Cai', 'Tỉnh'),
    ('Điện Biên', 'Tỉnh'),
    ('Lai Châu', 'Tỉnh'),
    ('Sơn La', 'Tỉnh'),
    ('Yên Bái', 'Tỉnh'),
    ('Hòa Bình', 'Tỉnh'),
    ('Thái Nguyên', 'Tỉnh'),
    ('Lạng Sơn', 'Tỉnh'),
    ('Quảng Ninh', 'Tỉnh'),
    ('Bắc Giang', 'Tỉnh'),
    ('Phú Thọ', 'Tỉnh'),
    ('Vĩnh Phúc', 'Tỉnh'),
    ('Bắc Ninh', 'Tỉnh'),
    ('Hải Dương', 'Tỉnh'),
    ('Hải Phòng', 'Thành Phố'),
    ('Hưng Yên', 'Tỉnh'),
    ('Thái Bình', 'Tỉnh'),
    ('Hà Nam', 'Tỉnh'),
    ('Nam Định', 'Tỉnh'),
    ('Ninh Bình', 'Tỉnh'),
    ('Thanh Hóa', 'Tỉnh'),
    ('Nghệ An', 'Tỉnh'),
    ('Hà Tĩnh', 'Tỉnh'),
    ('Quảng Bình', 'Tỉnh'),
    ('Quảng Trị', 'Tỉnh'),
    ('Thừa Thiên Huế', 'Tỉnh'),
    ('Đà Nẵng', 'Thành Phố'),
    ('Quảng Nam', 'Tỉnh'),
    ('Quảng Ngãi', 'Tỉnh'),
    ('Bình Định', 'Tỉnh'),
    ('Phú Yên', 'Tỉnh'),
    ('Khánh Hòa', 'Tỉnh'),
    ('Ninh Thuận', 'Tỉnh'),
    ('Bình Thuận', 'Tỉnh'),
    ('Kon Tum', 'Tỉnh'),
    ('Gia Lai', 'Tỉnh'),
    ('Đắk Lắk', 'Tỉnh'),
    ('Đắk Nông', 'Tỉnh'),
    ('Lâm Đồng', 'Tỉnh'),
    ('Bình Phước', 'Tỉnh'),
    ('Tây Ninh', 'Tỉnh'),
    ('Bình Dương', 'Tỉnh'),
    ('Đồng Nai', 'Tỉnh'),
    ('Bà Rịa - Vũng Tàu', 'Tỉnh'),
    ('Hồ Chí Minh', 'Thành Phố'),
    ('Long An', 'Tỉnh'),
    ('Tiền Giang', 'Tỉnh'),
    ('Bến Tre', 'Tỉnh'),
    ('Trà Vinh', 'Tỉnh'),
    ('Vĩnh Long', 'Tỉnh'),
    ('Đồng Tháp', 'Tỉnh'),
    ('An Giang', 'Tỉnh'),
    ('Kiên Giang', 'Tỉnh'),
    ('Cần Thơ', 'Thành Phố'),
    ('Hậu Giang', 'Tỉnh'),
    ('Sóc Trăng', 'Tỉnh'),
    ('Bạc Liêu', 'Tỉnh'),
    ('Cà Mau', 'Tỉnh')
)


def forwards_func(apps, schema_editor):
    Province = apps.get_model("vnprovinces", "Province")
    db_alias = schema_editor.connection.alias
    Province.objects.using(db_alias).bulk_create([
        Province(name=name, type=type)
        for name, type in provinces
    ])


def reverse_func(apps, schema_editor):
    Province = apps.get_model("vnprovinces", "Province")
    db_alias = schema_editor.connection.alias
    for name, type in provinces:
        Province.objects.using(db_alias).filter(name=name, type=type).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('vnprovinces', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]