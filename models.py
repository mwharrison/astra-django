from django.db import models


class Building(models.Model):
    astra_id = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name


class Classroom(models.Model):
    astra_id = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    modified = models.CharField(max_length=250)
    building = models.ForeignKey(Building)
    room_number = models.CharField(max_length=25)
    seats = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.building, self.room_number)
