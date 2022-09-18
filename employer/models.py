from django.db import models


class Company(models.Model):
    HIRE_TYPE = (
        ('direct', 'Direct'),
        ('temp-to-temp', 'Temp-to_Temp'),
        ('outsourcing', 'Outsourcing'),
        ('leasing', 'Leasing')
    )
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    contactPerson = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    numberOfWorkers = models.IntegerField(null=True, blank=True)
    hireType = models.CharField(choices=HIRE_TYPE, max_length=50, null=True, blank=True)
    NIP = models.CharField(max_length=10, null=True, blank=True)
    Regon = models.CharField(max_length=50, null=True, blank=True)
    KRS = models.CharField(max_length=50, null=True, blank=True)
    payAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('company-detail', kwargs={'slug': self.slug})


class Employee(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not decided', 'Not decided')
    )
    EDUCATION_CHOICES = (
        ('none', 'None'),
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('higher', 'Higher'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master')
    )

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=150)
    citizenship = models.CharField(max_length=50)
    image = models.FileField(upload_to='employees', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companies')
    education = models.CharField(choices=EDUCATION_CHOICES, max_length=50, blank=True, null=True)
    pesel = models.CharField(max_length=20, blank=True, null=True)
    passport_id = models.CharField(max_length=50, blank=True, null=True)
    karta_pobytu = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    last_entry_to_poland = models.DateField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'employee_id': self.pk})

    class Meta:
        ordering = ['-id',]
