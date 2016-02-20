from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=500)

class Team(models.Model):
    name = models.CharField(max_length=500)
    league_id = models.ForeignKey(League, null=True)
    user_id = models.ForeignKey(User, null=True)
    current_score = models.PositiveIntegerField(default=0)

class Law_Firm(models.Model):
    name = models.CharField(max_length=500)
    rank = models.PositiveIntegerField(default=0)
    points_earned = models.PositiveIntegerField(default=0)

class Team_Squishy(models.Model):
    team_id = models.ForeignKey(Team, null=True)
    firm_id = models.ForeignKey(Law_Firm, null=True)

class League(models.Model):
    name = models.CharField(max_length=500)

class Case(models.Model):
    case_number = models.CharField(max_length=500)
    defendant_firm = models.CharField(max_length=500)
    prosecutor_firm = models.CharField(max_length=500)
    status_id = models.ForeignKey(Status, null=True)

class Status(models.Model):
    case_status = models.BooleanField(default=False)

class Prosecutor_Firm(models.Model):
    case_id = models.ForeignKey(Case, null=True)
    firm_id = models.ForeignKey(Law_Firm, null=True)

class Defendant_Firm(models.Model):
    case_id = models.ForeignKey(Case, null=True)
    firm_id = models.ForeignKey(Law_Firm, null=True)
