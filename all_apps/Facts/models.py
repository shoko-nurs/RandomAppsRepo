
from django.conf import settings
from django.db import models



class Category(models.Model):

    category = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user_added = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False,db_constraint=False)

    def __str__(self):
        return f"{self.category.capitalize()} - {self.user_added}"

    def save(self, *args, **kwargs):
        self.category = self.category.lower()
        super(Category,self).save(*args, **kwargs)

class Fact(models.Model):

    from_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False, related_name="all_facts")
    fact = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user_added = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.fact}"

    class Meta:
        ordering = ['date_added']
