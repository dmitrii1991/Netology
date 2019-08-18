from django.db import models


class Phone(models.Model):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    system = models.CharField(max_length=50)
    color = models.CharField(max_length=50, null=True, blank=True)
    memory = models.IntegerField()
    screen_resolution = models.IntegerField()
    double_camera = models.BooleanField()
    screen_size = models.CharField(max_length=50)
    radio = models.BooleanField()

    def __repr__(self):
        return f'{self.name}'


class Iphone(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    face_id = models.BooleanField()

    def __repr__(self):
        return self.phone.name


class Samsung(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    stylus = models.BooleanField()
    double_screen = models.BooleanField()

    def __repr__(self):
        return self.phone.name


class Nokia(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    physical_keyboard = models.BooleanField()

    def __repr__(self):
        return self.phone.name