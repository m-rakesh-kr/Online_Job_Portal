from django.db import models
from django.utils import timezone

from accounts.models import company


Industry_List = (
    ('1', "Account"),
    ('2', "IT sales"),
    ('3', "Health Care"),
)


class Job(models.Model):
    company_name = models.ForeignKey(company, on_delete=models.CASCADE)
    company_website = models.CharField(max_length=100, default="")
    company_phoneo = models.TextField()
    company_address = models.CharField(max_length=150)
    company_city = models.CharField(max_length=150)
    company_state = models.CharField(max_length=150)
    company_country = models.CharField(max_length=150)
    Industry_list = models.CharField(choices=Industry_List, max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return self.title

class company(models.Model):
    user = models.ForeignKey(company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company.get_full_name()