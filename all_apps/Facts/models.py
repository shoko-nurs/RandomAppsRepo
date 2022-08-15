
from pyexpat import model
from django.conf import settings
from django.db import models



class Category(models.Model):

    category = models.CharField(max_length=100, blank=False, null=False)
    user_added = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False,db_constraint=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.user_added}"

    def save(self, *args, **kwargs):
        line = self.category.lower().capitalize().split()
        line = " ".join(line)
        self.category = line
        super(Category,self).save(*args, **kwargs)

    class Meta:
        unique_together=['category','user_added']
        ordering = ['-date_added']

class Fact(models.Model):

    from_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False, related_name="all_facts")
    fact = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user_added = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.fact}"

    class Meta:
        ordering = ['-date_added']
        unique_together = ['from_category','fact']


# class FactsAppIsPublic(models.Model):
#     is_publick = models.BooleanField(default=False)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)

#     def __str__(self):
#         return f"{self.user.email}-FactsApp-{self.is_publick}"
    
#     class Meta:
#         verbose_name = 'Facts App Publick'
#         verbose_name_plural = 'Facts App Publick Managing'