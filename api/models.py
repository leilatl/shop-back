from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
        }


