import datetime
from django.db import models
from django.utils import timezone

MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

GENDERS = models.IntegerChoices('Plec', 'Kobieta Mezczyzna Inna')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60, blank=False, null=False)
    opis = models.CharField(max_length=60, blank=True, null=True)


class Osoba(models.Model):

    imie = models.CharField(max_length=60, blank=False, null=False)
    nazwisko = models.CharField(max_length=60, blank=False, null=False)
    plec = models.IntegerField(choices=GENDERS.choices, default=GENDERS.choices[0][0])
    stanowisko = models.ForeignKey('Stanowisko', db_column='Stanowisko_nazwa', null=False, on_delete=models.DO_NOTHING)

