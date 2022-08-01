
from django.db import models



class Category(models.Model):

    category = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.category




class Fact(models.Model):

    from_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False, related_name="all_facts")
    fact = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fact}"

    class Meta:
        ordering = ['date_added']
