import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","immortalnews.settings")
import django
django.setup()

from immortalapp.models import *
from faker import Faker
from random import *
fake = Faker()

def phonenumbergen():
    d1= randint(6,9)
    num = ''+str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate =fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=("Python developer","Java Developer","PHP Developer"))
        felegibility = fake.random_element(elements=("BE/B.Tech","MCA","M.Tech"))
        faddress = fake.address()
        femail = fake.email()
        fcontact =phonenumbergen()
        hydjobs_record =Hyd_jobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, elegibility=felegibility,
                                                       address=faddress)
populate(25)