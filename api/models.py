from django.db import models

from django.db.models import Sum

from django.contrib.auth.models import User


class JobCard(models.Model):

    customer_name = models.CharField(max_length=200)

    phone=models.CharField(max_length=20)

    vehicle_number=models.CharField(max_length=200)

    running_kilometers=models.PositiveIntegerField()


    status_choices=(
        ("pending", "pending"),
        ("inprogress","inprogress"),
        ("completed","completed")
    )

    status=models.CharField(max_length=200,choices=status_choices,default="pending")

    created_date=models.DateTimeField(auto_now_add=True)

    @property
    def jobs(self):

        qs=Jobs.objects.filter(job_card_object=self)

        return qs
    
    @property
    def total_amount(self):

        total=self.jobs.values("amount").aggregate(total=Sum("amount"))["total"]

        return total
    

class Jobs(models.Model):

    title=models.CharField(max_length=200)

    notes=models.CharField(max_length=200)

    amount=models.PositiveIntegerField()

    job_card_object=models.ForeignKey(JobCard,on_delete=models.CASCADE)

    
   

    def __str__(self) -> str:
        return self.title
    



