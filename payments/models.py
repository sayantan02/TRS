from django.db import models
from students.models import *
# Create your models here.
class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    sub_payment_id = models.IntegerField(blank=True,null=True)
    payment_amount = models.IntegerField()
    order_id = models.CharField(max_length=120, blank=True,null=True)
    payment_id = models.CharField(max_length=120,blank=True,null=True)
    payment_signature = models.CharField(max_length=120,blank=True,null=True)
    is_paid = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-datetime',)

    def __str__(self) -> str:
        return self.student.name+" -- "+str(self.payment_amount)

class ScoutPayment(models.Model):
    student = models.ForeignKey(Student,models.CASCADE)
    training_fees = models.IntegerField(default=0)
    food_and_lodging_fees = models.IntegerField(default=0)
    uniform_fees = models.IntegerField(default=0)
    shoes_fees = models.IntegerField(default=0)
    ccrup_fees = models.IntegerField(default=0)
    cap_fees = models.IntegerField(default=0)
    belt_fees = models.IntegerField(default=0)
    admission_fees = models.IntegerField(default=0)
    membership_fees = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.student.name


