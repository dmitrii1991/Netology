from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def total_reviews(self):
        return self.review_count()

    total_reviews.short_description = "Всего отзывов"



class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
