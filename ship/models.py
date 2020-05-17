from django.db import models

class Ship(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MDO(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.quantity}m³ MDO remaining of {self.ship.name} ship.'


class FW(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.quantity}m³ FW remaining of {self.ship.name} ship.'