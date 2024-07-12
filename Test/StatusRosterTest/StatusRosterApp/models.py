from django.db import models
from django.contrib.auth.models import AbstractUser

class Cluster(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=30, unique=True)

class Member(AbstractUser):
    def __str__(self):
        return self.sap_id + " - " + self.last_name + ", " + self.first_name
    
    ROLES = {
        "A" : "Admin",
        "M" : "Manager",
        "U" : "User"
    }

    sap_id = models.CharField(max_length=7, unique=True)
    cluster_id = models.ForeignKey(Cluster, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=1, choices=ROLES)

class Status(models.Model):
    def __str__(self):
        return self.name
    
    type = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=30)

class Roster(models.Model):
    def __str__(self):
        return str(self.member_id) + " - " + str(self.date) + " - " + str(self.status)
    
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(max_length=100, blank=True)

class Log(models.Model):
    def __str__(self):
        return "[ " + str(self.member_id) + " ]" + " - [ " + str(self.roster_id) + " ] - " + str(self.timestamp)

    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    roster_id = models.ForeignKey(Roster, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
