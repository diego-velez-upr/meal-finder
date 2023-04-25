from django.db import models


class Food(models.Model):
    """
    Represents a single food item.
    """
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        """
        This is how each food will be displayed in the admin page.
        """
        return self.name
