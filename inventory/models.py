from django.db import models

# Create your models here.

class StaffRequest(models.Model):
    DEVICES = (
    ('Mon', 'Monitor'),
    ('CPU', 'Central Processing Unit'),
    ('KB', 'Keyboard'),
    ('Mou', 'Mouse'),
    )
    staff_name = models.CharField(max_length=20)
    staff_number = models.IntegerField(primary_key=True, unique=True)
    staff_department = models.CharField(max_length=15)
    r_equipment = models.CharField(max_length=3, choices=DEVICES, default='comp')

    def __str__(self):
        return self.staff_name
    class Meta:
        ordering = ('staff_number',)



class Equipment(models.Model):
    #= models.AutoField(primary_key=True)
    type = models.CharField(max_length=8)
    mac_address = models.CharField(max_length=20)
    serial_number= models.CharField(max_length=20)
    vendor = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    assigned_to = models.CharField(max_length=15, default='Not assigned')
    department = models.CharField(max_length=15, default='store')

    staffrequest = models.ForeignKey(StaffRequest, on_delete=models.CASCADE, default = 'None')

    class Meta:
        ordering = ('id',)
