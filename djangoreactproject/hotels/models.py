from django.db import models

class City(models.Model):
    name = models.CharField(verbose_name='название', max_length=20)

    def __str__(self):
        return self.name


class Hotels(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название', max_length=60)
    address = models.CharField(verbose_name='адрес', max_length=100)
    website = models.CharField(verbose_name='сайт', max_length=100, blank=True)
    email = models.CharField(verbose_name='email', max_length=50, blank=True)
    telephone = models.IntegerField(verbose_name='телефон', null=True)
    rating = models.IntegerField(verbose_name='рейтинг', null=True)

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class Comforts(models.Model):
    parking = models.BooleanField(verbose_name='парковка', default=False)
    transfer = models.BooleanField(verbose_name='трансфер', default=False)
    meals = models.BooleanField(verbose_name='питание', default=False)
    animation = models.BooleanField(verbose_name='анимация', default=False)
    fitness = models.BooleanField(verbose_name='фитнес', default=False)
    pool = models.BooleanField(verbose_name='бассейн', default=False)
    beach = models.BooleanField(verbose_name='пляж', default=False)
    spa = models.BooleanField(verbose_name='спа-комплекс', default=False)
    animals = models.BooleanField(verbose_name='животные', default=False)
    wifi = models.BooleanField(verbose_name='wifi', default=False)
    medical = models.BooleanField(verbose_name='медуслуги', default=False)


class HotelsComforts(models.Model):
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    comforts = models.ForeignKey(Comforts, on_delete=models.CASCADE)


class Rooms(models.Model):
    type = models.CharField(verbose_name='тип номера', max_length=20)
    price = models.DecimalField(verbose_name='цена номера', max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.type} ({self.price})"


class HotelsRooms(models.Model):
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)


class RoomsComforts(models.Model):
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    comforts = models.ForeignKey(Comforts, on_delete=models.CASCADE)

