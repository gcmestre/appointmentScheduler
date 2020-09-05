from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=80)
    birthdate = models.DateField(blank=True)
    comments = models.TextField(max_length=400, blank=True)
    phone_number = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    preferred_contact_method = models.CharField(max_length=1, choices=((None,None),
                                                                       ('cell_phone', 'cell_phone'),
                                                                       ('e-mail', 'email')))

    class Meta:
        abstract = True


class Client(Person):
    pass


class Employee(Person):
    job_title = models.CharField()


class AppointmentType(models.Model):

    type = models.CharField(max_length=40)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.type


class Appointment(models.Model):

    employee = models.ForeignKey(Employee)
    client = models.ForeignKey(Client)
    type = models.ForeignKey(AppointmentType)
    date = models.DateTimeField()
    comments = models.TextField(max_length=200, blank=True)
    payed = models.BooleanField(default=False)

    def __str__(self):
        return self.client.name + " - " + self.date
