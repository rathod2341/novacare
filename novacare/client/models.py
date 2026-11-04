from django.db import models

# Create your models here.

class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)

    class Meta:
        db_table = "area"

    def __str__(self):
        return self.area_name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=10)
    area_id = models.ForeignKey(Area,on_delete=models.CASCADE)
    otp = models.IntegerField()
    otp_used = models.IntegerField()
    
    class Meta:
        db_table = "patient"

    def __str__(self):
        return self.user_name

class specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    specialization_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = "specialization"

    def __str__(self):
        return self.specialization_name

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name= models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=10)
    location= models.CharField(max_length=150)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    open_time = models.TimeField()
    close_time = models.TimeField()
    profile_photo = models.ImageField(upload_to='doctor_profile/')
    sp_id = models.ForeignKey(specialization,on_delete=models.CASCADE)

    class Meta:
        db_table = "doctor"

    def __str__(self):
        return self.doctor_name

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    Appointment_date = models.DateField()
    Appointment_time = models.TimeField()
    status = models.CharField(max_length=20,default='pending')
    payment_status = models.CharField(max_length=20,default='pending')
    payment_mode = models.CharField(max_length=10)

    class Meta:
        db_table = "Appointment"

    def __str__(self):
        return f"Appointment {self.appointment_id} - {self.patient_id.user_name} with {self.doctor_id.doctor_name}"     

class galllery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to='gallery/')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        db_table = "gallery"

    def __str__(self):
        return f"Gallery {self.gallery_id} - {self.doctor_id.doctor_name}"  

class Review(models.Model):
    Review_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    review_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table= "review"
    
    def __str__(self):
        return f"Review {self.Review_id} - {self.patient_id.user_name} for {self.doctor_id.doctor_name}"

class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    services_value = models.CharField(max_length=20)
    basic_change = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        db_table = "services"

    def __str__(self):  
        return f"Service {self.service_id} - {self.services_value} by {self.doctor_id.doctor_name}"

