from django.db import models


# User-Register Model

ID_CHOICES =( 
        ("1", "PAN"), 
        ("2", "Aadhar"), 
        ("3", "VoterID"), 
        ("4", "Others"), 
    ) 

class Register(models.Model):
    name = models.CharField(max_length=100)
    idcard_no = models.IntegerField()
    id_type = models.CharField(max_length=1,choices=ID_CHOICES)
    address = models.TextField()
    phone_no = models.CharField(max_length=11)
    email = models.EmailField()
    meet_with = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Record of User Entry & Exit Model
class Entry(models.Model):
    person = models.ForeignKey(Register,null=True,on_delete=models.SET_NULL,related_name='RegisteredUsers')
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False)

