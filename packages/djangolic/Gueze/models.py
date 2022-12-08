from django.db import models

class Glass(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Beer Glasses"

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100,unique=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name
    def get_code(self):
        return self.code






# specialized kind of beer
class Style(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name




# general type of beer i.e lager, stout, etc..
class Type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name




class Beer(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    srm= models.CharField(max_length=8,blank=True,default="EBBB40",null=True)
    abv= models.FloatField(blank=True,null=True)
    ibu= models.FloatField(blank=True,null=True)
    image = models.CharField(max_length=2048,blank=True,null=True)
    brewery = models.ForeignKey('Brewery',related_name="beer-brewery+",on_delete=models.DO_NOTHING,blank=True,null=True)
    glass=models.ForeignKey(Glass,blank=True,on_delete=models.CASCADE,related_name='glass+',null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE,blank=True,null=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE,blank=True,null=True)
    taste = models.CharField(max_length=1500,blank=True,null=True)
    countries_sold_in = models.ManyToManyField(Country,related_name='countries_sold+',blank=True)

    def get_id(self):
        return self.id

    def get_countries(self):
        if(self.countries_sold_in.count() == 0):
            return ["Unknown"]
        
        return self.countries_sold_in.all()

    def get_srm(self):
        if(self.srm == None):
            return "Unknown"
        return "#" + self.srm
    
    
    def get_taste_short(self):
        if(self.taste == None):
            return "Unknown"
        return self.taste[:100] + "..."
        

    def __str__(self):
        return self.name

class Brewery(models.Model):
    name = models.CharField(max_length=50,blank=True,unique=True,null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,blank=True,null=True)
    beers = models.ManyToManyField(Beer,related_name="brewery-beers+",blank=True,null=True)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    
    def get_country(self):
        return self.country
    
    
    class Meta:
        verbose_name_plural = "Breweries"
