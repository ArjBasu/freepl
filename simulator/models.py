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

class players(models.Model):
    player_id = models.AutoField(primary_key = True)
    player_name = models.CharField("Player_Name",max_length = 50)
    player_country = models.CharField("Player_Country",max_length = 20)
    player_role = models.CharField("Player_Role",max_length = 20)
    player_bat_avg = models.FloatField("Batting_Average",default = 0.00)
    player_matches = models.IntegerField("Matches")
    player_runs = models.IntegerField("Runs")
    player_wickets = models.IntegerField("Wickets")
    player_bowl_avg = models.FloatField("Bowling_Average",default = "0.00")
    player_catches = models.IntegerField("Catches",default = 0)
    def __unicode__(self):
        return self.player_name
    
class performance(models.Model):
    performance_id = models.AutoField(primary_key = True)
    player_id = models.ForeignKey(players)
    day1= models.IntegerField("Day1",default = 0)
    day2= models.IntegerField("Day2",default = 0)
    day3= models.IntegerField("Day3",default = 0)
    day4= models.IntegerField("Day4",default = 0)
    day5= models.IntegerField("Day5",default = 0)
    day6= models.IntegerField("Day6",default = 0)
    day7= models.IntegerField("Day7",default = 0)
    day8= models.IntegerField("Day8",default = 0)
    day9= models.IntegerField("Day9",default = 0)
    day10= models.IntegerField("Day10",default = 0)
    def __unicode__(self):
        return self.player_id