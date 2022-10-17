from django.db import models
import json

from django.db.models import JSONField


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    _car_models = models.CharField(db_column="car_models", max_length=500)

    @property
    def car_models(self):
        return json.loads(self._car_models)

    @car_models.setter
    def car_models(self, x):
        self._car_models = json.dumps(x)


class TruckModel(models.Model):
    truck_name = models.CharField(max_length=100)

    def __str__(self):
        return self.truck_name


class TruckBrand(models.Model):
    brand_name = models.CharField(max_length=100)
    truck_models = models.ManyToManyField(TruckModel)
    ornek = JSONField()

    def __str__(self):
        return self.brand_name


if __name__ == '__main__':
    pass
    """First Solution of ListField"""
    # Save
    # sample_brand = Brand()
    # sample_brand.brand_name = "Mercedes"
    # sample_brand.car_models = ["c200", "c180", "e220d"]
    # sample_brand.save()

    # Get
    # sample_brand = Brand()
    # print(Brand.objects.get().car_models)
    # expected output: ['c200', 'c180', 'e220d']

    """ Second Solution of ListField"""
    # # Creation
    # ford = TruckBrand(brand_name="Ford")
    # ford.save()
    # truck_model_1 = TruckModel(truck_name="F150")
    # truck_model_1.save()
    # truck_model_2 = TruckModel(truck_name="F250")
    # truck_model_2.save()
    # truck_model_3 = TruckModel(truck_name="F350")
    # truck_model_3.save()
    #
    # # Relation
    # ford.truck_models.add(truck_model_1)
    # ford.truck_models.add(truck_model_2)
    # ford.truck_models.add(truck_model_3)
    # ford.save()
    #
    # # Get
    # print(ford.truck_models.last().truck_name)
    # # Expected output: 'F350'
