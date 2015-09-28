from datetime import datetime

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return "%s" % (self.name)


class Competition(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return "%s" % (self.name)


class Match(models.Model):
    winner = models.ForeignKey(Person, related_name='winned_matches')
    loser = models.ForeignKey(Person, related_name='loosed_matches')
    competition = models.ForeignKey(Competition, related_name='matches')
    time = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.time = datetime.now()
        return super(Match, self).save(*args, **kwargs)

    def __str__(self):
        return "%s defeats %s in %s" % (self.winner, self.loser, self.competition)
