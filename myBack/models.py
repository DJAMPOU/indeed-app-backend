from django.db import models

class Horaires_Roulements(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Type(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Publication(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    titre = models.CharField(max_length=100)
    entrepriseName = models.CharField(max_length=100)
    mail = models.CharField(max_length=50)
    emplacement = models.CharField(max_length=20)
    description = models.TextField()
    signaler = models.BooleanField()
    star = models.FloatField()
    manyOffer = models.BooleanField()
    haveHerSite = models.BooleanField()
    salaire = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.titre
    

class Employeur(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    entrepriseName = models.CharField(max_length=100)
    numbreEmployee = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    isManager = models.BooleanField(default=False)
    howDiscover = models.CharField(max_length=50)
    telNumber = models.CharField(max_length=20)

class Publi_Type(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    id_publi = models.ForeignKey(Publication, on_delete=models.CASCADE)
    id_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Publi_HR(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    id_publi = models.ForeignKey(Publication, on_delete=models.CASCADE)
    id_hr = models.ForeignKey(Horaires_Roulements, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
