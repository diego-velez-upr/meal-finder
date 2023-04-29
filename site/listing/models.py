from django.db import models


class Food(models.Model):
    """
    Represents a single food item.
    """
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    _tags = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='foods')

    def __str__(self):
        """
        This is how each food will be displayed in the admin page.
        """
        return self.name

    @property
    def tags(self):
        """
        Gets the list of tags of this food.
        """
        return self._tags.split(',')
