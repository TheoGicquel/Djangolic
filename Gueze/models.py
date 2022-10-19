from django.db import models



class style(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)

    def __unicode__(self):
        return self.name

class glass(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    asset_link = models.CharField(max_length=5000)

    def __unicode__(self):
        return self.name

class HexColor(models.Model):
    hex = models.CharField(max_length=10)

    def __unicode__(self):
        return self.hex

class srm(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=100)
    hex = models.ForeignKey(HexColor, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.color

class location(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name



class brewery(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    website = models.CharField(max_length=5000)
    update_at = models.DateField()
    location_brewery = models.ForeignKey(location, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name



class beer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    abv = models.FloatField()
    ibu = models.FloatField()
    logo = models.CharField(max_length=5000)

    #Foreignkey

    style = models.ManyToManyField(style)
    brasserie = models.ForeignKey(brewery, on_delete=models.CASCADE)
    srm = models.ForeignKey(srm, on_delete=models.CASCADE)
    glass = models.ForeignKey(glass, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
