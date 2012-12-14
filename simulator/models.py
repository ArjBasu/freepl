from django.db import models

# Create your models here.

class users(models.Model):
    user_id = models.AutoField(primary_key = True)
    user_name = models.CharField("UserName",max_length = 50)
    user_email = models.CharField("Email",max_length = 60)
    user_verified = models.BooleanField("Verified",default = "false")
    user_verification_id = models.CharField("Verification_Id",max_length = 100)
    user_bio = models.CharField("Bio",max_length = "200",default = "")
    user_dp = models.CharField("Profile Picture",max_length = "50",default = "")
    user_team = models.CharField("Team Name",max_length = "50",default = "")
    def __unicode__(self):
        return self.user_name
    