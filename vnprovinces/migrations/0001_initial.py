# Generated by Django 2.1.4 on 2019-02-21 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('Thành Phố', 'Thành Phố'), ('Tỉnh', 'Tỉnh')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('Quận', 'Quận'), ('Huyện', 'Huyện'), ('Thị Xã', 'Thị Xã'), ('Thành Phố', 'Thành Phố')], max_length=16)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='vnprovinces.Province'))
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('Phường', 'Phường'), ('Thị Trấn', 'Thị Trấn'), ('Xã', 'Xã')], max_length=16)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wards', to='vnprovinces.District')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='province',
            unique_together={('name', 'type')},
        ),
        migrations.AlterUniqueTogether(
            name='ward',
            unique_together={('name', 'type', 'district')},
        ),
        migrations.AlterUniqueTogether(
            name='district',
            unique_together={('name', 'type', 'province')},
        ),
    ]
