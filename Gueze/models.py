from django.db import models

class Glass(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name






class Location(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name



class Brewery(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    website = models.CharField(max_length=5000)
    update_at = models.DateField()
    location_brewery = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name




# general type of beer i.e lager, stout, etc..
class Type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


# more refined type of beer ex: irish stout, or other special kind of beer
class Style(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type,blank=True,on_delete=models.CASCADE,related_name="type+")
    def __str__(self):
        return self.name



class Beer(models.Model):
    name = models.CharField(max_length=100)
     
    desc= models.CharField(max_length=1500,blank=True)
    srm= models.CharField(max_length=8,blank=True,default="EBBB40")
    glass=models.ForeignKey(Glass,blank=True,on_delete=models.CASCADE,related_name='glass+')
    abv= models.IntegerField(blank=True)
    ibu= models.IntegerField(blank=True)
    style_name = models.CharField(max_length=100,blank=True)
    style_group = models.CharField(max_length=100,blank=True)
    taste= models.CharField(max_length=1500,blank=True)
    
        
    label_icon = models.CharField(max_length=2048,blank=True)
    label_medium = models.CharField(max_length=2048,blank=True)
    label_large = models.CharField(max_length=2048,blank=True)


    def __str__(self):
        return self.name + " " + self.desc
