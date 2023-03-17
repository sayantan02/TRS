from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

CHOICES = (
    ('COOCHBEHAR','Cooch Behar'),
    ('ALIPURDUAR','Alipurduar'),
)

class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=30, choices=CHOICES, default='COOCHBEHAR')
    course_fees = models.IntegerField()
    admission_fees = models.IntegerField()
    book_fees = models.IntegerField()
    puja_fees = models.IntegerField()
    dress_fees = models.IntegerField()
    registration_fees = models.IntegerField()
    icard_fees = models.IntegerField()
    bp_fees = models.IntegerField()
    opening_date = models.DateField()
    closing_date = models.DateField()
    picnic_fees = models.IntegerField()
    active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name+" -- "+self.course.name


PAYMENT_MODE = (
    ('CASH','Cash'),
    ('ONLINE','Online'),
)

ACTIVE_STATUS = (
    ('ACTIVE','Active'),
    ('IN_REVIEW','In Review'),
    ('INACTIVE','In Active')
)

class Student(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING,blank=True,null=True)
    applying_for = models.CharField(max_length=80,blank=True,null=True)
    status = models.CharField(max_length=30, choices=ACTIVE_STATUS, default='IN_REVIEW')
    name = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    whatsapp_number = models.IntegerField(blank=True,null=True)
    guardian_name = models.CharField(max_length=50)
    guardian_mobile_number = models.IntegerField()
    address = models.TextField()
    pin_code = models.CharField(max_length=20,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    adhaar_card = models.FileField(upload_to="adhaar_cards",blank=True,null=True)

    training_fees = models.IntegerField(default=0)
    food_and_lodging_fees = models.IntegerField(default=0)
    uniform_fees = models.IntegerField(default=0)
    shoes_fees = models.IntegerField(default=0)
    ccrup_fees = models.IntegerField(default=0)
    cap_fees = models.IntegerField(default=0)
    belt_fees = models.IntegerField(default=0)
    admission_fees = models.IntegerField(default=0)
    membership_fees = models.IntegerField(default=0)


    describe_queries = models.TextField(blank=True,null=True)
    payment_mode = models.CharField(max_length=30, choices=PAYMENT_MODE, default='ONLINE')
    picture = models.ImageField(upload_to="students")
    # date_of_admission = models.DateField(auto_now_add=True)
    admission_date = models.DateField(auto_now_add=True)
    
    # class Meta:
    #     ordering = ('-admission_date')

    def __str__(self) -> str:
        return self.name

class RegistrationNumber(models.Model):
    registration_number = models.CharField(max_length=90, unique=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    qr_code = models.CharField(max_length=90,blank=True,null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-datetime',)
        
    def __str__(self) -> str:
        return self.registration_number



