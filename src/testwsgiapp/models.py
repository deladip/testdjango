from datetime import date
from django.db import models
from django.forms import ModelForm


# Create your models here.

LIFE_TYPE =[
    ('TL', 'Term Life'),
    ('IUL', 'Index Universal'),
    ('WL', 'Whole Life'),
    ('FE', 'Final Expense'),
    ('FN', 'Foreign Nationals'),
    ('KE', 'Key Employee'),
]

HEALTH_TYPE =[
    ('IF', 'Individual and Family plans'),
    ('MP', 'Medicare Plans'),
    ('MA', 'Medicare Advantage'),
    ('MS', 'Medicare Supplement'),
    ('PD', 'Prescription Drug'),
    ('DP', 'Dental Plans'),
    ('VP', 'Vision Plans'),
]
HOW_YOU_HEARD_ABOUT_US =[
    ('phone', 'By phone'),
    ('Newspaper', 'News paper article'),
    ('mouth', 'Word of mouth'),
    ('social', 'Social Media outlet'),
    ('online', 'Online search e.g google'),
    ('marketer', 'Marketing outreach'),
]

IMMIGRATION_STATUS =[
    ('US', 'U.S Citizen'),
    ('LA','Legal Resident'),
    ('NA','Not Citizen or Resident ')
]


class CommonInfo(models.Model):
    first_name = models.CharField(max_length=26,null=True,blank=False)
    last_name = models.CharField(max_length=26, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    email = models.EmailField(blank=False)
    today_date = models.DateTimeField(default=date.today)
    
    class Meta:
        abstract = True

    
class ContactLIST(CommonInfo):
    calender = models.DateField(default=date.today)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    zip = models.CharField(max_length=5, verbose_name='Zip Code',blank=True)  
    how_you_heard_about_us = models.CharField(max_length=10, choices=HOW_YOU_HEARD_ABOUT_US)
    comments = models.TextField(max_length=200)     


class Health_Insurance_List(CommonInfo):
    quote_for = models.CharField(max_length=3, default=False, choices=HEALTH_TYPE)
    currently_insured = models.BooleanField(default=False)
    file_taxes_last_year = models.BooleanField(default=False)
    immigration_status = models.CharField(max_length=2,choices=IMMIGRATION_STATUS)

class Life_insurance_List(CommonInfo):
    currently_employed = models.BooleanField(default=False)
    annual_income = models.CharField(max_length=10,blank=False)
    quote_for = models.CharField(max_length=3,choices=LIFE_TYPE)
    note = models.TextField(verbose_name="Any additional info")

class ContactList_form(ModelForm):
    class Meta:
        model = ContactLIST
        fields = '__all__'

class Health_form(ModelForm):
    class Meta:
        model = Health_Insurance_List
        fields = '__all__'

class Life_form(ModelForm):
    class Meta:
        model = Life_insurance_List
        fields = '__all__'