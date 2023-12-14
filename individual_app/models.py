from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=200, default="title")
    is_active = models.BooleanField(default = False)
    about = models.TextField(blank = True)
    contact_email = models.CharField(max_length=200, blank = True)


class Member(models.Model):

#List of choices for major value in database, human readable name
    TITLE = (
('PRES', 'President of the PTA'),
('VICE', 'Vice President of the PTA'),
('SECY', 'Secretary of the PTA'),
('TRES', 'Treasure of the PTA'),
('MEM', 'Member of the PTA'),
)

    name = models.CharField(max_length=200)
    email = models.CharField("USER Email", max_length=200)
    title = models.CharField(max_length=200, choices=TITLE, blank = False)
    position = models.OneToOneField(Position, on_delete=models.CASCADE, unique=True)
