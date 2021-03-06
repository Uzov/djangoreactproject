# Generated by Django 3.2.12 on 2022-03-26 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='название')),
            ],
        ),
        migrations.CreateModel(
            name='Comforts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking', models.BooleanField(default=False, verbose_name='парковка')),
                ('transfer', models.BooleanField(default=False, verbose_name='трансфер')),
                ('meals', models.BooleanField(default=False, verbose_name='питание')),
                ('animation', models.BooleanField(default=False, verbose_name='анимация')),
                ('fitness', models.BooleanField(default=False, verbose_name='фитнес')),
                ('pool', models.BooleanField(default=False, verbose_name='бассейн')),
                ('beach', models.BooleanField(default=False, verbose_name='пляж')),
                ('spa', models.BooleanField(default=False, verbose_name='спа-комплекс')),
                ('animals', models.BooleanField(default=False, verbose_name='животные')),
                ('wifi', models.BooleanField(default=False, verbose_name='wifi')),
                ('medical', models.BooleanField(default=False, verbose_name='медуслуги')),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='название')),
                ('address', models.CharField(max_length=100, verbose_name='адрес')),
                ('website', models.CharField(blank=True, max_length=100, verbose_name='сайт')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='email')),
                ('telephone', models.IntegerField(null=True, verbose_name='телефон')),
                ('rating', models.IntegerField(null=True, verbose_name='рейтинг')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.city')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='тип номера')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='цена номера')),
            ],
        ),
        migrations.CreateModel(
            name='RoomsComforts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comforts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.comforts')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='HotelsRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='HotelsComforts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comforts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.comforts')),
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels')),
            ],
        ),
    ]
