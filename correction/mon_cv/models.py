from django.db import models

# Create your models here.

class Civility(models.Model):
    civ = models.CharField(max_length=20)

class SkillCat(models.Model):
    category = models.CharField(max_length=50)

class User(models.Model):
    civ_id = models.ForeignKey(Civility, on_delete=models.CASCADE)
    bithday = models.DateField()
    mail = models.CharField(max_length=250)
    address = models.CharField(max_length=300)

class Skills(models.Model):
    cat_id = models.ForeignKey(SkillCat, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    describe = models.CharField(max_length=1024)
