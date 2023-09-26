from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class NidhiEIR(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = PhoneNumberField(blank=True)
    dateOfBirth = models.DateField()
    address = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    ideaDescription = models.TextField()

    gen = (
        ('Male',"Male"),
        ('Female', "Female"),
        ('Prefer Not to Say', "Prefer Not to Say"),
    )
    gender = models.CharField(max_length=20, choices=gen, default="None")

    cat = (
        ('General',"General"),
        ('OBC', "OBC"),
        ('SC', "SC"),
        ('ST', "ST"),
    )
    category = models.CharField(max_length=10, choices=cat, default='None')


    resume = models.FileField(upload_to='resumes/')
    conceptNote = models.FileField(upload_to='notes/')
    aspectNote = models.FileField(upload_to='notes/')

    choice = (
        ('Yes','Yes'),
        ('No','No'),
    )

    previousRecipient = models.CharField(max_length=10, choices= choice)
    fullCommitment = models.CharField(max_length=10, choices= choice)
    noOtherFellowship = models.CharField(max_length=10, choices= choice)
    businessCommitment = models.CharField(max_length=10, choices= choice)
    notBeneficiary = models.CharField(max_length=10, choices= choice)
    registerPEP = models.CharField(max_length=10, choices= choice)


    def __str__(self):
        return self.name


    